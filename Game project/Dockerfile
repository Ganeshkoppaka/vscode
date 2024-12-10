# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies specified in requirements.txt
# (If you have dependencies, create a requirements.txt file in the same folder as the Dockerfile)
#COPY requirements.txt .
#RUN pip install -r requirements.txt

# Run the Python script when the container launches
CMD ["python", "main.py"]
