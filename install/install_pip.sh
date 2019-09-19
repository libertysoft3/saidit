#!/bin/bash

# load configuration
RUNDIR=$(dirname $0)
source $RUNDIR/install.cfg

cat <<PACKAGES | xargs pip install -U pip
wheel
captcha
cryptography
pyopenssl
stripe
tinycss2
httpagentparser
haigha
PyJWT
Babel
py-bcrypt
whoosh
PACKAGES

# alternative https://launchpad.net/~reddit/+archive/ubuntu/ppa/+files/python-pycaptcha_0.4-1_all.deb
pushd $REDDIT_SRC
wget -nc https://s3.amazonaws.com/code.reddit.com/pycaptcha-0.4.tar.gz
pip install -U pip pycaptcha-0.4.tar.gz
popd