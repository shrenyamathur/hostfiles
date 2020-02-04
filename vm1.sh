#!/bin/sh
mkdir uploadfiles
cd uploadfiles
Git clone https://github.com/shrenyamathur/hostfiles
cd hostfiles
sudo ufw allow 5000/tcp
sudo apt-get update
sudo apt-get install python-pip
pip install azure.storage
pip install flask
Python azure103_project.py
