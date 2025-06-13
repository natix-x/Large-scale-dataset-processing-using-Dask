#!/bin/bash

python -m venv venv

echo "Activating virtual environment..."
source venv/bin/active

echo "Installing requirements..."

python -m pip install --upgrade pip

pip install -r requirements.txt