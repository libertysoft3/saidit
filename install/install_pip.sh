#!/bin/bash

# load configuration
RUNDIR=$(dirname $0)
source $RUNDIR/install.cfg

# TODO PORT - need $ sudo rm -rf /usr/local/lib/python2.7/dist-packages/OpenSSL/ before pyopenssl will install? cyptography lib.
pip install -U pip wheel captcha cryptography pyopenssl stripe tinycss2 httpagentparser haigha PyJWT posix_ipc Babel