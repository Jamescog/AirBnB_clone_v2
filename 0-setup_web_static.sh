#!/usr/bin/env bash
# create folders if not exist
slink="/data/web_static/current"
s_file="/data/web_static/releases/test/"
s=("/data/" "/data/web_static/" "/data/web_static/releases/" "/data/web_static/shared/" "/data/web_static/releases/test/")
for fol in ${s[@]}
do
    if [ ! -d $fol ]
    then
        sudo mkdir -p $fol
    fi
done
sudo touch /data/web_static/releases/test/index.html
sudo tee /data/web_static/releases/test/index.html<<EOF
<h1> Hello Everybody </h1>
<p>I am excited to see the <em>end</em> of this stuff</p>
EOF
if [ -L $slink ]
then
    sudo rm $slink
    sudo ln -s $s_file $slink
else
    sudo ln -s $s_file $slink
fi
ln -s /etc/nginx/sites-available/default config
sudo chown -R ubuntu:ubuntu /data/
sudo tee config<<EOF
server {
    listen 80;
    server_name localhost;
    root /var/www/html;
    index index.html;
    error_page 404 /custom_404.html;
    location = /custom_404.html {
        root /var/www/error;
        internal;
    }
    location /something/ {
        try_files something  =404;
    }
    location /hbnb_static {
        alias /data/web_static/current/;
    }
    add_header X-Served-By $HOSTNAME;
     location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

}
EOF
sudo service nginx reload
