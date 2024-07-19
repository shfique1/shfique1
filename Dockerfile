# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy the Python dependencies file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script to the working directory
COPY SinglePageScrap.py .

# Install Chrome browser and chromedriver
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && wget https://chromedriver.storage.googleapis.com/92.0.4515.107/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/local/bin/ \
    && rm chromedriver_linux64.zip \
    && chmod +x /usr/local/bin/chromedriver

# Set Chrome options environment variable (optional)
ENV CHROME_BIN=/usr/bin/google-chrome \
    CHROME_DRIVER=/usr/local/bin/chromedriver

# Run the Python script when the container launches
CMD ["python", "SinglePageScrap.py"]


