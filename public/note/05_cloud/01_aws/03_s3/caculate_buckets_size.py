import boto3

def calculate_s3_usage():
    # Use the high-level 'resource' API for cleaner code
    s3 = boto3.resource('s3')
    
    total_account_size = 0
    
    print(f"{'Bucket Name':<40} {'Size (MB)':>12} {'Size (GB)':>12}")
    print("-" * 66)

    # Loop through all buckets
    for bucket in s3.buckets.all():
        bucket_size_bytes = 0
        
        # .objects.all() automatically handles pagination for you
        # Warning: This can take time if a bucket has millions of objects
        try:
            for obj in bucket.objects.all():
                bucket_size_bytes += obj.size
        except Exception as e:
            print(f"{bucket.name:<40} {'ACCESS DENIED':>25}")
            continue

        # Convert to MB and GB
        size_mb = bucket_size_bytes / (1024 ** 2)
        size_gb = bucket_size_bytes / (1024 ** 3)
        
        total_account_size += bucket_size_bytes
        
        print(f"{bucket.name:<40} {size_mb:>12.2f} {size_gb:>12.2f}")

    print("-" * 66)
    print(f"TOTAL ACCOUNT USAGE: {total_account_size / (1024**3):.2f} GB")

if __name__ == "__main__":
    calculate_s3_usage()