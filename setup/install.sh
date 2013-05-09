#!/usr/bin/bash

cp setup/gunicorn.conf /etc/supervisor/conf.d/
service supervisor restart
supervisorctl start gunicorn

rm -f /etc/nginx/sites-enabled/default
cp setup/nginx /etc/nginx/sites-available/fermenter

ln -s /etc/nginx/sites-available/fermenter /etc/nginx/sites-enabled/fermenter
service nginx restart

crontab setup/cron.txt
