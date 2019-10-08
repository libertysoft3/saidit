#!/bin/bash

sudo -u reddit make build/mangle-buildstamp
sudo -u reddit make clean_css
sudo -u reddit make css
sudo reddit-flush
sleep 10
sudo service reddit-paster restart
sudo service reddit-paster2 restart
sudo service reddit-paster3 restart
sudo service reddit-paster4 restart