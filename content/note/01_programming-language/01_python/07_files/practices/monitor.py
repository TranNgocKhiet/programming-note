import subprocess
import os

server_list = []
server_file = "servers.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(current_directory, server_file)
output_file = os.path.join(current_directory, "uptime_report.txt")

if not os.path.exists(input_file):
    print(f"File not found: {input_file}")
else:
    with open(input_file) as file:
        for line in file:
            server_list.append(line.strip())
    
    if not server_list:
        print(f"No server found in {server_file}")
    else: 
        with open(output_file, "a") as file:
            for server_name in server_list:
                command = ["ping", "-n", "1", server_name]
                result = subprocess.run(command, capture_output=True, text=True)
                
                if result.returncode == 0:
                    print(f"✅ {server_name} is ONLINE")
                    file.write(f"{server_name} is ONLINE\n")
                else:
                    print(f"❌ {server_name} is OFFLINE")
                    file.write(f"{server_name} is OFFLINE\n")
            