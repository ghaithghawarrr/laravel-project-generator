# Use a base image with Python and PHP pre-installed
FROM php:8.1-cli

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    unzip \
    && apt-get clean

# Install Composer globally
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install required PHP extensions for Laravel
RUN docker-php-ext-install pdo pdo_mysql

# Install Python libraries
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

# Copy the script and related files
COPY . /app/

# Set the default command to execute your script
CMD ["python3", "your_script.py"]
