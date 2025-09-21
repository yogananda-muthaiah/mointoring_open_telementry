# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy monitoring script
COPY monitor.py .

# Run monitoring service
CMD ["python", "monitor.py"]
