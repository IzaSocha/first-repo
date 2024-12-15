FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app.py ./

# Expose the port that the app runs on
EXPOSE 80

# Define the command to run the application
CMD ["python", "app.py"]
