# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any dependencies specified in requirements.txt
RUN apt-get update && \
    apt-get install -y pkg-config default-libmysqlclient-dev libmariadb-dev build-essential \
    && \
    pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port that the app runs on
EXPOSE 8000
EXPOSE 3306

# Run the command to start the Django server
CMD ["python", "homeServiceApp/manage.py", "migrate", "0.0.0.0:8000"]
#