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

### ✅ **Thank you for using Job Search Automation!**
💡 **Found this useful? Give it a ⭐ on GitHub!** 🚀
