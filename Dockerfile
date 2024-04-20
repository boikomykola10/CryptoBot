# Use a slim Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy your bot script
COPY bot.py .

# Set the entrypoint to run your bot script
ENTRYPOINT ["python", "bot.py"]
