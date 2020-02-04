#!/bin/sh
sudo apt-get update
sudo apt-get install apache2
mkdir newfiles
cd newfiles
git clone https://github.com/shrenyamathur/hostfiles
cd hostfiles
sudo cp default.html /var/www/html
sudo cp index.html /var/www/html
