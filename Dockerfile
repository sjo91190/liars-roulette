# Use Python as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the app code to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

ENV LIARS_CONFIG=prod

# Run the Flask app with Waitress
CMD ["python", "roulette.py"]
