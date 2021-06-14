#install nginx\\
sudo apt-get install nginx
#install php7.4
sudo apt update
sudo apt upgrade
sudo apt install software-properties-common
sudo add-apt-repository ppa:ondrej/php
sudo apt update
sudo apt install php7.4-fpm
sudo apt install php7.4-common php7.4-mysql php7.4-xml php7.4-xmlrpc php7.4-curl php7.4-gd php7.4-imagick php7.4-cli php7.4-dev php7.4-imap php7.4-mbstring php7.4-opcache php7.4-soap php7.4-zip php7.4-intl php7.4-pgsql -y
 #install postgresql
sudo -s
echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list
wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add –
apt-get update
apt-get install postgresql-contrib-12 -y
apt-get install postgresql-12 -y
echo "listen_addresses='*'" >> /etc/postgresql/12/main/postgresql.conf
echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/12/main/pg_hba.conf
service postgresql restart
exit
 #setup psql
sudo -i -u postgres
psql
CREATE USER <username> WITH PASSWORD '<password>'; replace with user/password
ALTER USER <username> CREATEDB;
\q
exit
#modify nginx config file
cd /etc/nginx/sites-enabled
sudo nano default
 
change the content to following:
 server {
      listen 80;
      listen [::]:80;
      root #this would be your farmOS /web directory
      index  index.php index.html index.htm;
      server_name  localhost #for local development

      location / {
          try_files $uri /index.php?$query_string;        
      }

      location @rewrite {
              rewrite ^/(.*)$ /index.php?q=$1;
          }

      location ~ [^/]\.php(/|$) {
          include snippets/fastcgi-php.conf;
          fastcgi_pass unix:/var/run/php/php7.1-fpm.sock;
          fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
          include fastcgi_params;
      }

      location ~ ^/sites/.*/files/styles/ { # For Drupal >= 7
              try_files $uri @rewrite;
      }

      location ~ ^(/[a-z\-]+)?/system/files/ { # For Drupal >= 7
          try_files $uri /index.php?$query_string;
      }
  }
  
  service nginx restart
 
cd  <web folder>: sites/default
mkdir files
chmod 777 files
cp default.settings.php settings.php
chmod 777 settings.php
 
sudo -i -u postgres
psql
ALTER DATABASE "postgres" SET bytea_output = 'escape';

