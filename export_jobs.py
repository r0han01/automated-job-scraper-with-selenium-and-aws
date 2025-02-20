import csv
import os
import boto3
from datetime import datetime
import os  # ✅ Import os for environment variables
# S3 Bucket Name
BUCKET_NAME = "job-search-results"

# AWS S3 Client Setup
s3_client = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_KEY")
)

def export_jobs_to_s3(job_list, job_title, location):
    """Exports job data to CSV and uploads it to Amazon S3, then returns the file URL."""
    
    if not job_list:
        print("❌ No jobs to export.")
        return None

    # Generate filename (with date & time)
    date_time_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Includes time
    filename = f"{job_title}_{location}_{date_time_str}.csv".replace(" ", "_")  # Replace spaces with underscores

    # Save locally (temporary)
    local_file_path = f"/tmp/{filename}"

    try:
        # Write data to CSV
        with open(local_file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["Job Title", "Posted By", "Location", "Salary"])
            writer.writeheader()
            writer.writerows(job_list)

        print(f"✅ CSV file saved locally: {local_file_path}")

        # Upload CSV to S3
        s3_client.upload_file(local_file_path, BUCKET_NAME, filename)
        s3_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"
        print(f"🚀 CSV uploaded to S3: {s3_url}")

        # Cleanup: Remove local temp file
        os.remove(local_file_path)
        print("🧹 Local temp file deleted.")

        return s3_url  # Return S3 file URL

    except Exception as e:
        print(f"❌ Error exporting jobs to S3: {e}")
        return None
