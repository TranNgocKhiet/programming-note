import boto3

BUCKET_NAME = "fcj-smart-office-test-upload-v1" # Use the name you created earlier
REGION = "ap-southeast-1"

s3 = boto3.resource('s3', region_name=REGION)
bucket = s3.Bucket(BUCKET_NAME)

print(f"preparing to delete {BUCKET_NAME}...")

# Step 1: Check if bucket exists
if bucket.creation_date:
    # Step 2: Delete all objects inside (The "Emptying" phase)
    # bucket.objects.all() gives us a list of every file
    print(" - Deleting all objects inside...")
    bucket.objects.all().delete()
    
    # Step 3: Delete the bucket itself
    print(" - Deleting the bucket itself...")
    bucket.delete()
    
    print("✅ Cleanup complete. Bucket is gone.")
else:
    print("⚠️ Bucket does not exist. Nothing to do.")