#!/bin/sh

#manual steps:
# install git
# clone fermenter repository

#apt-get update
#apt-get install -y nginx python-dev
#curl -O http://python-distribute.org/distribute_setup.py
#python distribute_setup.py
#curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
#python get-pip.py
#sudo pip install virtualenv
#cd Fermenter
#virtualenv env
#pip install -r requirements.txt

#run ./manage.py syncdb
#./manage.py migrate



cp gunicorn.conf /etc/supervisor/conf.d/
service supervisor restart
supervisorctl start gunicorn

rm -f /etc/nginx/sites-enabled/default
cp nginx /etc/nginx/sites-available/fermenter

ln -s /etc/nginx/sites-available/fermenter /etc/nginx/sites-enabled/fermenter
service nginx restart

crontab cron.txt
