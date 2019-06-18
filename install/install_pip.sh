#!/bin/bash

# load configuration
RUNDIR=$(dirname $0)
source $RUNDIR/install.cfg

# TODO - have to do a sudo rm -rf /usr/local/lib/python2.7/dist-packages/OpenSSL/ before pyopenssl would install??? cyptography lib
# TODO  - support (python-support) is there for old cassandra only and has lots of hard dependencies
pip install -U pip wheel captcha cryptography stripe tinycss2 httpagentparser haigha pyopenssl
