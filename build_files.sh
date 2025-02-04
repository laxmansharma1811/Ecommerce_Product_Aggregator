#!/bin/bash

# Ensure Python and pip are installed
apt update && apt install -y python3 python3-pip

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
