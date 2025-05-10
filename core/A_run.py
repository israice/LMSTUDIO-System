import os

# Get absolute path to project root (parent directory of this script)
project_folder = os.path.dirname(os.path.abspath(__file__))

# Change working directory to project root
os.chdir(project_folder)

# List of scripts to run
scripts = [
    "AA_open.py",
    "AB_close.py",
]

# Run each script from the project root
for script in scripts:
    script_path = os.path.join(project_folder, script)
    os.system(f"python {script_path}")
