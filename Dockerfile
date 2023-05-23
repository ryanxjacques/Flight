# Author: Ryan
# Description: This Dockerfile defines the build process for the Docker image.

# Use the base Python image with pip3 included.
FROM python:3.11.3

# Set the working directory inside the container to /django/.
WORKDIR /django/

# Copy the requirements.txt file from the current directory to the container's workdir.
COPY requirements.txt .

# Install the dependencies.
# (--no-cache-dir) => Avoid using the cache directory for downloaded package files to enhance reproducibility and avoid caching errors.
# (-r requirements.txt) => Instruct pip to read and install the dependencies specified in the requirements.txt file.
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy all the files from the current directory to the container's workdir.
COPY . .

# Expose the necessary ports (8000 for the Django development server).
EXPOSE 8000:8000

# Define the command that will be run when the Docker container starts
CMD python3 manage.py runserver 0.0.0.0:8000

