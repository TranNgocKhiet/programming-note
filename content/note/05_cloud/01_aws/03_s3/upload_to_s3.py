import boto3
from botocore.exceptions import ClientError
import os

# --- CONFIGURATION ---
# 1. CHANGE THIS to a unique name (e.g., "yourname-devops-practice-2025")
BUCKET_NAME = "fcj-smart-office-test-upload-v1" 
REGION = "ap-southeast-1" # Singapore region (best for Vietnam)
FILE_NAME = "hello_aws.txt"

# Initialize Client
s3 = boto3.client('s3', region_name=REGION)

def create_bucket_if_not_exists():
    """Checks if bucket exists. If not, creates it safely."""
    print(f"Checking status of '{BUCKET_NAME}'...")
    
    try:
        # head_bucket asks: "Does this exist and do I have access?"
        s3.head_bucket(Bucket=BUCKET_NAME)
        print(f"✅ Bucket '{BUCKET_NAME}' already exists. Moving on...")
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        
        if error_code == '404':
            # 404 means "Not Found" -> We need to create it
            print(f"⚠️ Bucket not found. Creating '{BUCKET_NAME}' in {REGION}...")
            
            try:
                s3.create_bucket(
                    Bucket=BUCKET_NAME,
                    CreateBucketConfiguration={'LocationConstraint': REGION}
                )
                print(f"✅ Success: Bucket created!")
                
            except ClientError as create_error:
                print(f"❌ Failed to create bucket: {create_error}")
                return False
                
        else:
            # Some other error (e.g., 403 Forbidden - someone else owns this name)
            print(f"❌ Error checking bucket: {e}")
            print("Tip: S3 names must be globally unique. Try a different name.")
            return False
            
    return True

# --- MAIN EXECUTION ---

# Step 1: Check/Create Bucket
if create_bucket_if_not_exists():
    
    # Step 2: Create dummy file locally
    with open(FILE_NAME, "w") as f:
        f.write(f"Hello! This file lives in {BUCKET_NAME} now.")

    # Step 3: Upload
    print(f"Uploading {FILE_NAME}...")
    try:
        s3.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)
        print("✅ Upload Complete! Go check your AWS Console.")
    except Exception as e:
        print(f"❌ Upload Failed: {e}")