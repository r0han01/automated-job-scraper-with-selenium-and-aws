from flask import Flask, render_template, request, jsonify
import threading
import boto3
import csv
import io
import os  # ✅ Import os for environment variables
from selenium_scraper import start_selenium
from export_jobs import export_jobs_to_s3

app = Flask(__name__)

# ✅ AWS S3 Setup using environment variables
BUCKET_NAME = "job-search-results"
s3_client = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_KEY")
)

@app.route('/')
def home():
    """Render the job search input form."""
    return render_template('selenium_job_bot.html')

@app.route('/search_jobs', methods=['POST'])
def search_jobs():
    """Receive job title and location from AJAX request and start Selenium automation."""
    data = request.json
    job_title_input = data.get('job_title')
    location_input = data.get('location')

    if not job_title_input or not location_input:
        return jsonify({'error': '❌ Missing job title or location'}), 400

    print(f"✅ Received job search request for: {job_title_input} in {location_input}")

    def run_selenium():
        scraped_jobs = start_selenium(job_title_input, location_input)
        if scraped_jobs:
            s3_url = export_jobs_to_s3(scraped_jobs, job_title_input, location_input)
            print(f"✅ File uploaded to S3: {s3_url}")

    # Start Selenium in a separate thread
    selenium_thread = threading.Thread(target=run_selenium)
    selenium_thread.start()

    response_message = "✅ Automation started successfully!"
    print(response_message)  # ✅ Print message in terminal

    return jsonify({'message': response_message})

@app.route('/view_jobs')
def view_jobs():
    """Fetch the latest job CSV from S3 and display it with the formatted template."""
    try:
        # Get list of objects from S3 bucket
        objects = s3_client.list_objects_v2(Bucket=BUCKET_NAME)

        if 'Contents' not in objects:
            return "❌ No job files found in S3.", 404

        # Get the latest uploaded file
        latest_file = max(objects['Contents'], key=lambda x: x['LastModified'])
        file_key = latest_file['Key']

        # Extract job title and location from filename
        filename_parts = file_key.replace(".csv", "").split("_")
        job_title = " ".join(filename_parts[:-2])  # Everything except last 2 parts
        location = filename_parts[-2]

        # Fetch file from S3
        obj = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_key)
        csv_data = obj['Body'].read().decode('utf-8')

        # Read CSV data
        jobs = []
        csv_reader = csv.DictReader(io.StringIO(csv_data))
        for row in csv_reader:
            jobs.append({
                "title": row["Job Title"],
                "company": row["Posted By"],
                "location": row["Location"],
                "salary": row["Salary"]
            })

        return render_template(
            'job_listings.html',
            job_title=job_title,
            location=location,
            jobs=jobs
        )

    except Exception as e:
        return f"❌ Error fetching jobs from S3: {e}"

if __name__ == '__main__':
    app.run(debug=True)
