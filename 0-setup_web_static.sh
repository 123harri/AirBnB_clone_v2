#!/usr/bin/env bash

# Update package repositories
sudo apt-get update

# Install Nginx
sudo apt-get -y install nginx

# Allow Nginx through firewall
sudo ufw allow 'Nginx HTTP'

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
sudo echo "<html>
<head>
</head>
<body>
  Holberton School
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Set ownership
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx
sudo service nginx restart
