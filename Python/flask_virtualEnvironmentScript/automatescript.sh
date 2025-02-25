#!/bin/bash
#Purpose: # python script to create virtual environment,activate it,
            # install dependencies through requirements.txt file already there and 
            # run helloworld.py file of flask which is also in same folder
            # Check if Python3 is available
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install it."
    exit 1
fi

# Create a virtual environment named 'venv'
python3 -m venv myvenv

# Activate the virtual environment
source myvenv/bin/activate

# Check if requirements.txt exists and install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found!"
    exit 1
fi

# Check if helloworld.py exists and run it
if [ -f "helloworld.py" ]; then
    echo "Running helloworld.py..."
    python helloworld.py
else
    echo "helloworld.py not found!"
    exit 1
fi