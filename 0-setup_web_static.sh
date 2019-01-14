#!/usr/bin/env bash
# Installs nginx, creates folders, and updates nginx to serve content from one folder
sudo apt-get update
sudo apt-get -y install nginx
mkdir -p "/data/web_static/releases/test"
mkdir -p "/data/web_static/shared/"
touch /data/web_static/releases/test/index.html
echo "Testing this file" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown --recursive ubuntu:ubuntu /data/
wget https://raw.githubusercontent.com/VortexH/AirBnB_clone_v2/master/third_config
cp third_config /etc/nginx/sites-available/default
sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo service nginx start
