#!/usr/bin/env bash
# Script sets up web server for deployment

# installs Nginx
apt-get -y update
apt-get -y upgrade
apt-get -y install nginx

# creates folders /data/web_static/releases/test/
mkdir -p /data/web_static/releases/test/

# creates /data/web_static/shared/
mkdir -p /data/web_static/shared/

# Create fake html file with basic content
echo '
<!DOCTYPE html>
<html>
<head>
<title>REAL MADRID</title>
</head>
<body>

<h1>My HALA MADRID</h1>
<p>tengo mucha hambre.</p>

</body>
</html> ' > /data/web_static/releases/test/index.html

# creates a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Gives ownership to the ubuntu user and group
chown -hR ubuntu:ubuntu /data/

# Updates nginx configuration to server
sed -i '40i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# restarts nginx
service nginx restart
