# Use an official Python runtime as the base image
FROM python:3.9

WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose the port on which the application will run
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
