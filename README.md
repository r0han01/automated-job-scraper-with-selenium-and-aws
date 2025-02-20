## **Job Search Automation with Selenium & AWS S3**

**Automated Job Scraper** using **Selenium, Flask, and AWS S3** to fetch real-time job listings from **Adzuna** and store them in **Amazon S3**. The results are displayed dynamically on a web page.
###
![ScreenShot Tool -20250220005805](https://github.com/user-attachments/assets/69bc7d48-fd4b-4ac8-b444-e11810cd9718)
###

## **Features**
- **Automated Job Search** → Uses **Selenium** to scrape job listings from Adzuna.
- **Dynamic Web UI** → Built with **Flask & Jinja2 Templates**.
- **Data Export to AWS S3** → Saves job listings as **CSV files** in an S3 bucket.
- **Real-Time Job Display** → Fetches and displays job results dynamically.
- **Browser Automation** → Handles pop-ups, cookies, and user interactions.
- **Multi-Threading** → Ensures **efficient background automation**.

---

## **Technologies Used**
| Technology  | Purpose |
|------------|---------|
| **Python** | Core programming language |
| **Selenium** | Web scraping for job listings |
| **Flask** | Web framework for UI |
| **AWS S3** | Cloud storage for CSV results |
| **Boto3** | AWS SDK for Python |
| **HTML/CSS (Jinja2)** | Frontend for job display |
| **JavaScript (AJAX)** | Handles search requests |
| **Chromedriver (Brave)** | Automates browser |

---

## **📂 Project Structure**
```
selenium_job_bot_project/
│── app.py                  # Main Flask app
│── config.py               # Configuration (AWS keys, browser paths)
│── selenium_scraper.py      # Selenium automation script
│── export_jobs.py           # Exports jobs to AWS S3
│── static/
│   ├── css/style.css       # Custom styling
│   ├── js/script.js        # JavaScript for search functionality
│── templates/
│   ├── selenium_job_bot.html  # Main job search UI
│   ├── job_listings.html      # Displays job results
│── env/                     # Python virtual environment (ignored in .gitignore)
│── __pycache__/             # Compiled Python files (ignored)
│── .gitignore               # Excludes sensitive files
│── README.md                # This file
```

---

## **How It Works**
### **Step 1: User Searches for Jobs**
- The Flask web app provides an input form.
- The user enters a **Job Title** and **Location**.
- AJAX sends the request to the **Flask backend**.
###
![Screenshot from 2025-02-20 01-05-13](https://github.com/user-attachments/assets/862770f9-f408-49b0-b599-7b6d6058ab03)
###
![ScreenShot Tool -20250220005921](https://github.com/user-attachments/assets/097baad5-aa75-435b-89c4-23df9d94724b)
###

### **Step 2: Selenium Automates Job Scraping**
- **Selenium opens Brave Browser** and navigates to **Adzuna**.
- It searches for **latest jobs** based on the user's input.
- Pop-ups and cookies are handled **automatically**.
- Extracted jobs are **logged & stored in a list**.
# This is a Automated Process You Dont Even Need To Touch Mouse After Hitting The Button, Watch Below Video !!
###
![Screencastfrom2025-02-2001-08-32-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/d4be3aca-0663-4c2b-9205-f74527c292c7)
###
![Screenshot from 2025-02-20 01-14-57](https://github.com/user-attachments/assets/a1a41384-6d45-433a-a858-966b6036e66c)
###
### **Step 3: Export to AWS S3**
- Scraped jobs are **saved as a CSV file**.
- The file is named in the format:  
  ```
  Job_Title_Location_YYYY-MM-DD_HH-MM.csv
  ```
###
![Screenshot from 2025-02-20 01-22-39](https://github.com/user-attachments/assets/c2a858fa-b355-4c9d-b2d8-aed48076928e)
###
- The file is **uploaded to AWS S3**.
###
![ScreenShot Tool -20250220012805](https://github.com/user-attachments/assets/f7538690-dffb-49e4-961e-beaac76ec069)
###
![Screenshot from 2025-02-20 01-32-26](https://github.com/user-attachments/assets/773cdc56-929a-4af4-b8ef-585c37316b03)
###
### **Step 4: Display Results**
- The Flask app fetches the CSV from S3.
- The job listings are **displayed dynamically**.
###
![ScreenShot Tool -20250220014113 (1)](https://github.com/user-attachments/assets/5babbfba-dc5e-4e5e-b0c8-b1b057558b5d)
###
---

## **Functions & Key Components**
| Function  | Purpose |
|------------|---------|
| **`start_selenium(job_title, location)`** | Starts Selenium and scrapes jobs |
| **`monitor_popups()`** | Handles pop-ups & cookies |
| **`export_jobs_to_s3(job_list, job_title, location)`** | Saves jobs as CSV and uploads to AWS S3 |
| **`fetch_csv_from_s3(job_title, location)`** | Retrieves the latest CSV from S3 |
| **`view_jobs()`** | Flask route to display job listings |

---

## **Setup & Installation**
### **Step 1: Clone the Repository**
```bash
git clone https://github.com/r0han01/automated-job-scraper-with-selenium-and-aws.git
cd automated-job-scraper-with-selenium-and-aws
```

### **Step 2: Create Virtual Environment**
```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 4: Configure AWS & Selenium**
- **Edit `config.py`** and add:
  ```python
  AWS_ACCESS_KEY = "your-access-key"
  AWS_SECRET_KEY = "your-secret-key"
  BRAVE_PATH = "/path/to/brave-browser"
  CHROMEDRIVER_PATH = "/path/to/chromedriver"
  PROFILE_DIR = "/path/to/selenium-profile"
  ```
- Ensure **AWS credentials** are correctly configured.

### **Step 5: Run Flask App**
```bash
python app.py
```
- Open **http://127.0.0.1:5000/** in your browser.

---

## **📜 Commands Reference**
| Command  | Description |
|------------|---------|
| `python app.py` | Runs the Flask web server |
| `python selenium_scraper.py` | Runs job scraping manually |
| `python export_jobs.py` | Exports jobs to AWS S3 |
| `git status` | Check modified files |
| `git add .` | Stage all changes |
| `git commit -m "Your message"` | Commit changes |
| `git push origin main` | Push code to GitHub |


---
### **🔹 Key Features & Importance of This Selenium Job Scraper**

This script is a **fully automated job scraper** that interacts with the Adzuna job search website using **Selenium**, processes the job listings, and stores them **securely in AWS S3**. It also **automatically opens a web page** to display the extracted job data.

---

### **📌 1. Automating Job Search with Selenium**
We use Selenium to **simulate user input**, enter job details, and fetch listings dynamically.

#### ✅ **Code Snippet: Automating Search**
```python
search_box = driver.find_element(By.XPATH, '//*[@id="what"]')
search_box.clear()
search_box.send_keys(job_title_input)

location_box = driver.find_element(By.XPATH, '//*[@id="where"]')
location_box.clear()
location_box.send_keys(location_input)
location_box.send_keys(Keys.RETURN)
```
**🔹 Why is this Important?**
- **Eliminates manual searches** by automatically inputting job title & location.
- Uses **XPath selectors** to interact with search boxes dynamically.
- **Ensures fast, accurate job retrieval** with `send_keys()`.

---

### **📌 2. Handling Pop-ups & Cookies Efficiently**
Web automation often requires handling **unexpected pop-ups and cookie banners**, which can block the process. We use **threaded background monitoring** to continuously check for pop-ups.

#### ✅ **Code Snippet: Background Monitoring**
```python
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
```
**🔹 Why is this Important?**
- **Prevents UI blockages** caused by modal pop-ups.
- Runs in a **separate thread**, allowing the scraper to continue uninterrupted.
- Ensures **smooth, error-free execution** in different browsing environments.

---

### **📌 3. Extracting Job Listings Dynamically**
We retrieve job details such as **title, company, location, and salary** dynamically from the webpage.

#### ✅ **Code Snippet: Extracting Jobs**
```python
job_titles = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/main/article/div[2]/div[1]/h2/a')
posted_bys = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/main/article/div[2]/div[2]/div[1]/a')
packages = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/main/article/div[2]/div[2]/div[3]/a[1]')
locations = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/main/article/div[2]/div[2]/div[2]')

for title, posted_by, package, location in zip(job_titles, posted_bys, packages, locations):
    print(f"🔹 Job Title - {title.text}")
    print(f"🏢 Posted By - {posted_by.text}")
    print(f"📍 Location - {location.text}")
    print(f"💰 Job Worth - {package.text}")
```
**🔹 Why is this Important?**
- **Extracts real-time job data** dynamically, keeping results fresh.
- Uses **XPath selectors** for precise element identification.
- Stores jobs in a structured format for **easy processing & storage**.

---

### **📌 4. Storing Job Listings in AWS S3**
After fetching the job data, we **export it as a CSV file** and upload it securely to AWS S3.

#### ✅ **Code Snippet: Uploading to S3**
```python
export_jobs_to_s3(scraped_jobs, job_title_input, location_input)
```
**🔹 Why is this Important?**
- **Prevents data loss** by storing files in **cloud storage**.
- **Enables remote access** to job data from any device.
- **Scales efficiently**, handling large amounts of job listings.

---

### **📌 5. Automatically Opening Job Listings Page**
Once the scraping is complete, the script **automatically opens the job listings in the browser**.

#### ✅ **Code Snippet: Opening Web Page**
```python
webbrowser.open("http://127.0.0.1:5000/view_jobs")
```
**🔹 Why is this Important?**
- **Enhances user experience** by directly opening the results.
- **Eliminates manual navigation**, saving time.
- **Ensures real-time job updates** are visible instantly.

---

### **📌 6. Handling Browser Closure Gracefully**
The script properly **handles manual browser closures**, ensuring clean termination of processes.

#### ✅ **Code Snippet: Handling Manual Closure**
```python
try:
    driver.quit()
    print("✅ Browser closed successfully.")
except WebDriverException:
    print("🛑 Browser was already closed manually.")
```
**🔹 Why is this Important?**
- Prevents **crashes** due to unexpected browser shutdowns.
- Ensures **graceful script termination** for stability.
- Keeps **system resources optimized** by closing unused processes.

---

### **✨ Conclusion: Why This Automation is Powerful**
This script combines **automation, web scraping, cloud storage, and dynamic web rendering** to build a **scalable job search assistant**. 

🚀 **Key Takeaways:**
- **Selenium** automates job searches and extracts data in real-time.
- **Background monitoring** handles pop-ups and cookies seamlessly.
- **AWS S3 storage** ensures **secure, cloud-based** job data management.
- **Flask integration** dynamically displays **latest job results**.
- **Automated browser opening** enhances user convenience.

💡 **This isn't just a scraper—it's a full-fledged job search assistant that works autonomously!** 🚀

### ✅ **Thank you for using Job Search Automation!**
💡 **Found this useful? Give it a ⭐ on GitHub!** 🚀
