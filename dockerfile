# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable to avoid buffering issues
ENV PYTHONUNBUFFERED 1

# Run app.py when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "demo_web_app.wsgi:application"]
