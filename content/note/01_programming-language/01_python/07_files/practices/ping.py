import subprocess

host = "google.com"
command = ["ping", "-n", "1", host]

result = subprocess.run(command, capture_output=True, text=True)

print(f"Output: {result.stdout}\n")
print(f"Exit: {result.returncode}")