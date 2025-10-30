# Use the official lightweight Python image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy your project files
COPY . /app

# (Optional) Install dependencies if requirements.txt exists
# RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run your calculator
CMD ["python", "withHistory.py"]
