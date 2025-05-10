import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the project folder from .env (strict mode)
project_folder = os.getenv('PROJECT_FOLDER')
if not project_folder:
    raise ValueError("PROJECT_FOLDER is not set in .env file")

scripts = [
    "A_run.py",
]

# Record the start time
start_time = time.time()

for script in scripts:
    script_path = os.path.join(project_folder, script)
    os.system(f"python {script_path}")

# Calculate and print the total execution time
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Total execution time: {elapsed_time:.2f} seconds")
