# Use the official Python base image with the desired version
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

COPY ../requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN apt-get -y install build-essential

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get upgrade -y && apt-get clean

# Copy the entire app directory into the container at /app
COPY . .

# Expose the port that the app runs on
EXPOSE 8050

# Define the command to run your application using gunicorn as a production server
CMD ["gunicorn", "-b", "0.0.0.0:8050", "app:server"]