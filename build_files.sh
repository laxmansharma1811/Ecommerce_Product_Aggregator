#!/bin/bash

# Install dependencies
pip3 install -r requirements.txt

# Run Django migrations
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic --noinput
