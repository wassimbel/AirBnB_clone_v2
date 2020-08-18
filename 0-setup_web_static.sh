#!/usr/bin/env bash
# sets up web servers for deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
sudo service nginx start
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '45i \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n}' /etc/nginx/sites-available/default
sudo service nginx restart
