import datetime
import os
# Get current time
current_time = datetime.datetime.now()

# TODO: Open "logs/access.log" in APPEND mode ("a")
# Write the string: f"[{current_time}] User logged in\n"
folder_name = "logs"

if (os.path.exists(folder_name) == False):
    os.mkdir(folder_name)
    print(f"Folder {folder_name} created!")

with open("logs/access.log", "a") as file:  # <--- Fill in the mode
    file.write(f"[{current_time}] User logged in\n")
    
    print("Log entry added.")
