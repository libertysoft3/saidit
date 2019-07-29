#!/bin/bash

# load configuration
RUNDIR=$(dirname $0)
source $RUNDIR/install.cfg

git clone https://github.com/apache/thrift.git
cd thrift
git checkout v0.12.0
./bootstrap.sh
./configure
make
sudo make install

git clone https://github.com/reddit/baseplate.git
cd baseplate
git checkout v0.30.3
make
sudo -u $REDDIT_USER python setup.py build