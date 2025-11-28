import os

folder_name = "logs"
file_name = "server.log"
full_path = os.path.join(folder_name, file_name)

if not os.path.exists(full_path):
    print(f"{full_path} not found")
else:
    with open(f"{full_path}", "r") as file:
        for line in file:
            if ("ERROR" in line):
                print(f"{line.strip()}")