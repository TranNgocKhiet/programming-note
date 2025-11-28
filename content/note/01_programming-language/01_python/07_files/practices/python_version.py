import subprocess

# The command we want to run: "python --version"
# We pass it as a list: ["command", "argument"]
command = ["python", "--version"]

# Run it!
result = subprocess.run(command, capture_output=True, text=True)

# result.stdout = The standard output (success message)
# result.returncode = 0 means success, anything else means error
print(f"Output: {result.stdout}")
print(f"Exit Code: {result.returncode}")