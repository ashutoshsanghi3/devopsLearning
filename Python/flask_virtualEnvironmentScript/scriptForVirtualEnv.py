# python script to create virtual environment,activate it,
# install dependencies through requirements.txt file already there and 
# run helloworld.py file of flask which is also in same folder
import os
import subprocess
import sys

# Path for virtual environment
venv_name = 'venv'

# Check if virtualenv exists, if not, create it
if not os.path.exists(venv_name):
    print("Creating virtual environment...")
    subprocess.check_call([sys.executable, '-m', 'venv', venv_name])

# Activate the virtual environment
activate_script = os.path.join(venv_name, 'Scripts', 'activate')

print(f"Activating the virtual environment from {activate_script}")
subprocess.check_call([activate_script], shell=True)

# Install dependencies from requirements.txt
if os.path.exists('requirements.txt'):
    print("Installing dependencies from requirements.txt...")
    subprocess.check_call([os.path.join(venv_name, 'Scripts', 'pip'), 'install', '-r', 'requirements.txt'])
else:
    print("No requirements.txt file found.")

# Running the Flask app (helloworld.py)
if os.path.exists('helloworld.py'):
    print("Running the Flask application (helloworld.py)...")
    subprocess.check_call([os.path.join(venv_name, 'Scripts', 'python.exe'), 'helloworld.py'])
else:
    print("No helloworld.py file found.")
