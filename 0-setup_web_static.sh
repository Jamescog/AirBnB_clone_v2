#!/usr/bin/env bash
# configure brandnew ubuntu for deployment
sudo apt-get -y update
sudo apt-get -y install nginx
slink="/data/web_static/current"
s_file="/data/web_static/releases/test/"
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
sudo tee /data/web_static/releases/test/index.html<<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF
if [ -L $slink ]
then
    sudo rm $slink
    sudo ln -s $s_file $slink
else
    sudo ln -s $s_file $slink
fi
sudo chown -R ubuntu:ubuntu /data/
sudo tee /etc/nginx/sites-a*/de*<<EOF
server {
    listen 80;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html;
    error_page 404 /custom_404.html;
    location = /custom_404.html {
        root /var/www/error;
        internal;
    }
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html;
    }
    add_header X-Served-By $HOSTNAME;
     location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}
EOF
sudo service nginx reload
