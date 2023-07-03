# Use an official Python runtime as the base image
FROM python:3.7-slim

WORKDIR /tarsus_backend

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN apt-get update

# Install Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .
CMD flask db init ; \
flask db stamp head && \
flask db migrate && \
flask db upgrade && \
gunicorn --workers 2 --timeout 120 -b 0.0.0.0:5000 --reload tarsus:app