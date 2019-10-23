#!/bin/bash

sudo -u reddit make build/mangle-buildstamp
sudo -u reddit make clean_css
sudo -u reddit make css
sleep 5
sudo service reddit-paster restart
