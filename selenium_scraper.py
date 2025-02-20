import shutil
import os
import threading
import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from config import BRAVE_PATH, CHROMEDRIVER_PATH, PROFILE_DIR
from export_jobs import export_jobs_to_s3  # ✅ Import AWS S3 export function
import webbrowser


# Global flag to track if monitoring should continue
monitoring = True

def start_selenium(job_title_input, location_input):
    """Run Selenium automation to search for jobs on Adzuna."""
    
    global monitoring
    monitoring = True  # Start monitoring

    # Set Chrome options
    options = Options()
    options.binary_location = BRAVE_PATH  
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--disable-gpu")
    options.add_argument(f"--user-data-dir={PROFILE_DIR}")
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36")
    options.add_argument("--incognito")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Set up ChromeDriver service
    service = Service(CHROMEDRIVER_PATH)

    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://www.adzuna.com")
        time.sleep(3)  # Ensure page is loaded

        def close_popup():
            try:
                popup_close = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[1]/a")
                if popup_close:
                    popup_close.click()
                    print("✅ Pop-up closed successfully.")
            except NoSuchElementException:
                pass
            except WebDriverException:
                print("🛑 Browser closed manually. Stopping pop-up interaction...")

        def decline_cookies():
            try:
                decline_button = driver.find_element(By.XPATH, '//*[@id="cookiescript_reject"]')
                decline_button.click()
                print("✅ Cookies rejected successfully.")
                time.sleep(2)
            except NoSuchElementException:
                pass

        def monitor_popups():
            global monitoring
            while monitoring:
                try:
                    if driver.session_id:
                        close_popup()
                        decline_cookies()
                    else:
                        break
                except WebDriverException:
                    print("🛑 Browser was closed manually. Stopping pop-up monitoring...")
                    break
                time.sleep(1)

        popup_thread = threading.Thread(target=monitor_popups, daemon=True)
        popup_thread.start()

        # Enter job title
        try:
            search_box = driver.find_element(By.XPATH, '//*[@id="what"]')
            search_box.clear()
            search_box.send_keys(job_title_input)
            print(f"✅ Entered Job Title: {job_title_input}")
        except NoSuchElementException:
            print("❌ Unable to find job title input box!")

        # Enter job location
        try:
            location_box = driver.find_element(By.XPATH, '//*[@id="where"]')
            location_box.clear()
            location_box.send_keys(location_input)
            location_box.send_keys(Keys.RETURN)
            print(f"✅ Entered Job Location: {location_input}")
        except NoSuchElementException:
            print("❌ Unable to find job location input box!")

        time.sleep(5)  # Wait for results to load

        # Click on "Date Posted" filter
        try:
            date_posted_filter = driver.find_element(By.XPATH, '//*[@id="filters"]/div/div/a[2]/h2')
            date_posted_filter.click()
            time.sleep(2)

            last_3_days = driver.find_element(By.XPATH, '//*[@id="date_posted"]/div/a[2]')
            last_3_days.click()
            time.sleep(5)
            print("✅ Filtered jobs for 'Last 3 Days'.")
        except NoSuchElementException:
            print("❌ Unable to filter by date posted!")

        # Extract job postings
        scraped_jobs = []  # Store job data in a list of dictionaries

        try:
            job_titles = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/main/article/div[2]/div[1]/h2/a')
            posted_bys = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/main/article/div[2]/div[2]/div[1]/a')
            packages = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/main/article/div[2]/div[2]/div[3]/a[1]')
            locations = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/main/article/div[2]/div[2]/div[2]')

            if not job_titles:
                print("❌ No job listings found!")

            for title, posted_by, package, location in zip(job_titles, posted_bys, packages, locations):
                print(f"🔹 Job Title - {title.text}")
                print(f"🏢 Posted By - {posted_by.text}")
                print(f"📍 Location - {location.text}")
                print(f"💰 Job Worth - {package.text}")
                print("-" * 50)

                # Store in dictionary for CSV export
                job_data = {
                    "Job Title": title.text,
                    "Posted By": posted_by.text,
                    "Location": location.text,
                    "Salary": package.text
                }
                scraped_jobs.append(job_data)

            # ✅ Export jobs to S3
            export_jobs_to_s3(scraped_jobs, job_title_input, location_input)

            webbrowser.open("http://127.0.0.1:5000/view_jobs")


        except NoSuchElementException:
            print("❌ Unable to extract job postings!")

        # Wait for user input to close browser
        try:
            input("🔍 Press Enter to close the browser...")
        except KeyboardInterrupt:
            print("\n🛑 Browser quit manually via keyboard interrupt.")

    except WebDriverException:
        print("\n🛑 Browser closed manually by user!")

    except Exception as e:
        print(f"❌ Selenium Error: {e}")
        traceback.print_exc()

    finally:
        monitoring = False  # Stop pop-up monitoring

        if os.path.exists(PROFILE_DIR):
            shutil.rmtree(PROFILE_DIR)
            print(f"✅ User profile directory {PROFILE_DIR} cleared successfully.")

        try:
            driver.quit()
            print("✅ Browser closed successfully.")
        except WebDriverException:
            print("🛑 Browser was already closed manually.")
