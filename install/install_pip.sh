#!/bin/bash

# load configuration
RUNDIR=$(dirname $0)
source $RUNDIR/install.cfg

pip install -U pip wheel captcha cryptography pyopenssl stripe tinycss2 httpagentparser haigha PyJWT posix_ipc Babel py-bcrypt whoosh PyCAPTCHA

# wget https://s3.amazonaws.com/code.reddit.com/pycaptcha-0.4.tar.gz
# pip install -U pip pycaptcha-0.4.tar.gz 