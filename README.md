Fermenter
=========

A Raspberry Pi powered fermentation chamber for brewing beer with a simple and slick web interface.


Long Installation Instructions
============

### Install OS packages: ###

    sudo apt-get install vim python-dev python-setuptools nginx supervisor git
    sudo easy_install pip
    sudo pip install virtualenv virtualenvwrapper
    echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
    source /usr/local/bin/virtualenvwrapper.sh


### Install Fermenter Web Application ###

    cd ~
    mkvirtualenv fermenter
    git clone https://github.com/mfwarren/Fermenter.git
    cd Fermenter
    pip install -r requirements.txt
    ./manage.py syncdb
    ./manage.py migrate
    ./manage.py runserver 0.0.0.0:8000

Test that the webserver is working on port 8000 before proceeding, Ctrl-C to stop server once confirmed.

### Configure Http Server ###

I'm using nginx infront of gunicorn (managed by supervisord). The config files are included.

    sudo python setup/install.py

set hostname on raspberry pi:

    sudo vim /etc/hostname

replace 'raspberrypi' with 'fermenter'

Reboot

    sudo reboot


