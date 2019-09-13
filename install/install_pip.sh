#!/bin/bash

# load configuration
RUNDIR=$(dirname $0)
source $RUNDIR/install.cfg

# TODO PORT need posix_ipc ??
cat <<PACKAGES | xargs pip install -U pip
cmake
autoconf
libssl-dev
libboost-all-dev
libevent-dev
flex
bison
libbison-dev
libgoogle-glog-dev
libdouble-conversion-dev
scons
libkrb5-dev
libsnappy-dev
liblz4-dev
libiberty-dev
liblzma-dev
binutils-dev
libjemalloc-dev
PACKAGES

# alt https://launchpad.net/~reddit/+archive/ubuntu/ppa/+files/python-pycaptcha_0.4-1_all.deb
pushd $REDDIT_SRC
wget -nc https://s3.amazonaws.com/code.reddit.com/pycaptcha-0.4.tar.gz
pip install -U pip pycaptcha-0.4.tar.gz
popd