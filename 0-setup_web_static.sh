#!/usr/bin/env bash
# sets up web servers for deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
sudo service nginx start
if [[ ! -d /data/ ]]; then
    sudo mkdir /data/
fi
if [[ ! -d /data/web_static/ ]]; then
    sudo mkdir -p /data/web_static/
fi
if [[ ! -d /data/web_static/releases ]]; then
    sudo mkdir -p /data/web_static/releases/
fi
if [[ ! -d /data/web_static/shared ]]; then
    sudo mkdir -p /data/web_static/shared/
fi
if [[ ! -d /data/web_static/releases/test/ ]]; then
    sudo mkdir -p /data/web_static/releases/test
fi
if [[ ! -f /data/web_static/releases/test/index.html ]]; then
    sudo touch /data/web_static/releases/test/index.html
    echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
fi
if [[ -h /data/web_static/current ]]; then
    sudo rm -rf /data/web_static/current
    sudo ln -s /data/web_static/releases/test/ /data/web_static/current
elif [[ ! -h /data/web_static/current ]]; then
    sudo ln -s /data/web_static/releases/test/ /data/web_static/current
fi
sudo chown ubuntu:ubuntu /data/

sudo sed -i '45i \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n}' /etc/nginx/sites-enabled/default
sudo service nginx restart
