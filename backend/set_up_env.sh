#!/bin/bash

# Check if Python3 is installed
if ! command -v python3 &>/dev/null; then
  echo "Python3 is not installed. Please install it."
  exit 1
fi

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install required packages
pip install asgiref==3.7.2
pip install Django==4.2.4
pip install django-uuidfield==0.5.0
pip install mysqlclient==2.2.0
pip install Pillow==10.0.0
pip install sqlparse==0.4.4
pip install typing_extensions==4.7.1
pip install uuid==1.30

# Deactivate the virtual environment
deactivate

echo "Environment setup completed. You can activate it with 'source venv/bin/activate'."
