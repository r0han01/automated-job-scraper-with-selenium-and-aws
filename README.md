
## **Job Search Automation with Selenium & AWS S3**

**Automated Job Scraper** using **Selenium, Flask, and AWS S3** to fetch real-time job listings from **Adzuna** and store them in **Amazon S3**. The results are displayed dynamically on a web page.

## ** Features**
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

### **Step 2: Selenium Automates Job Scraping**
- **Selenium opens Brave Browser** and navigates to **Adzuna**.
- It searches for **latest jobs** based on the user's input.
- Pop-ups and cookies are handled **automatically**.
- Extracted jobs are **logged & stored in a list**.

### **Step 3: Export to AWS S3**
- Scraped jobs are **saved as a CSV file**.
- The file is named in the format:  
  ```
  Job_Title_Location_YYYY-MM-DD_HH-MM.csv
  ```
- The file is **uploaded to AWS S3**.

### **Step 4: Display Results**
- The Flask app fetches the CSV from S3.
- The job listings are **displayed dynamically**.

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
