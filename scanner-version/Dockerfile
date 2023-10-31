FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy your Python script into the container
COPY cve-latestVersion.py .

# Make port 8080 available to the world outside this container
EXPOSE 8082

# Run custom-exporter.py when the container launches
CMD ["python", "cve-latestVersion.py"]

