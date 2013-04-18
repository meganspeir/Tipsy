#!/bin/bash
#

PROJECT_NAME='tipsy'

# Install PIP via Distribute
cd /tmp/
curl -O http://python-distribute.org/distribute_setup.py
python distribute_setup.py
easy_install pip
sudo rm /tmp/*.gz
sudo rm /tmp/*.py

# Install git
sudo apt-get install -y git

# Twitter Bootstrap
# git clone git://github.com/twitter/bootstrap.git

# Update some stuff.
sudo apt-get update

# Install SQLite3
sudo apt-get install sqlite3

# Install requirements
sudo pip install -r /Developer/Projects/$PROJECT_NAME/requirements.txt
