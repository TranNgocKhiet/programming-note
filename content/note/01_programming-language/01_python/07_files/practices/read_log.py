import os

folder_name = "logs"
log_count = 0
if not os.path.exists(folder_name):
    print(f"Folder {folder_name} not found!")
else:
    with open("logs/access.log", "r") as file:
        for line in file:
            print(f"Read line: {line.strip()}")
            log_count += 1

print(f"Log count: {log_count}")