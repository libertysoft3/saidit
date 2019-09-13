#!/bin/bash
# The contents of this file are subject to the Common Public Attribution
# License Version 1.0. (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://code.reddit.com/LICENSE. The License is based on the Mozilla Public
# License Version 1.1, but Sections 14 and 15 have been added to cover use of
# software over a computer network and provide for limited attribution for the
# Original Developer. In addition, Exhibit A has been modified to be consistent
# with Exhibit B.
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for
# the specific language governing rights and limitations under the License.
#
# The Original Code is reddit.
#
# The Original Developer is the Initial Developer.  The Initial Developer of
# the Original Code is reddit Inc.
#
# All portions of the code written by reddit are Copyright (c) 2006-2015 reddit
# Inc. All Rights Reserved.
###############################################################################

# load configuration
RUNDIR=$(dirname $0)
source $RUNDIR/install.cfg

# add the datastax cassandra repos (NB: this is required for
# install_cassandra.sh to work correctly, and the non-existence of this
# file will trigger install_cassandra.sh to rerun this script)
echo deb http://debian.datastax.com/community stable main | \
    sudo tee $CASSANDRA_SOURCES_LIST
    
wget -qO- -L https://debian.datastax.com/debian/repo_key | \
    sudo apt-key add -

echo deb https://facebook.github.io/mcrouter/debrepo/bionic bionic contrib | \
    sudo tee $FACEBOOK_SOURCES_LIST

wget -qO- -L https://facebook.github.io/mcrouter/debrepo/bionic/PUBLIC.KEY | \
    sudo apt-key add -

# grab the new ppas' package listings
# run an aptitude update to make sure python-software-properties
# dependencies are found
apt-get update
apt-get $APTITUDE_OPTIONS upgrade

# travis gives us a stock libmemcached.  We have to remove that
apt-get remove $APTITUDE_OPTIONS $(dpkg-query  -W -f='${binary:Package}\n' | grep libmemcached | tr '\n' ' ')
apt-get autoremove $APTITUDE_OPTIONS

# install prerequisites
cat <<PACKAGES | xargs apt-get install $APTITUDE_OPTIONS
software-properties-common
netcat-openbsd
git

python-dev
python-pip
python-setuptools
python-routes
python-pylons
python-boto
python-tz
python-crypto
python-numpy
python-dateutil
cython
python-sqlalchemy
python-beautifulsoup
python-chardet
python-psycopg2
python-pil
python-amqplib
python-bcrypt
python-snappy
gperf

python-lxml
python-kazoo
python-unidecode
python-mock
python-yaml

python-flask
geoip-bin
geoip-database
python-geoip

nodejs
node-less
node-uglify
gettext
make
optipng
jpegoptim

libpcre3-dev

python-gevent
python-gevent-websocket

python-redis
python-pyramid
python-raven

libssl-dev
g++
cmake
make
automake
pkg-config
libevent-dev
libdouble-conversion-dev
libgoogle-glog-dev
libgflags-dev
libiberty-dev
liblz4-dev
liblzma-dev
libsnappy-dev
libxml2-dev
libxslt1-dev
zlib1g-dev
binutils-dev
libjemalloc-dev
libzstd-dev
libffi-dev
python-cffi
mcrouter
PACKAGES

# fbthrift dependencies
cat <<PACKAGES | xargs apt-get install $APTITUDE_OPTIONS
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

# cassandra
pushd $REDDIT_SRC
wget -nc http://archive.ubuntu.com/ubuntu/pool/universe/p/python-support/python-support_1.0.15_all.deb
apt-get install $APTITUDE_OPTIONS ./python-support_1.0.15_all.deb
popd

# pycassa
# 'apt-get install python-pycassa' will remove python-fbthrift and install
# python-thrift which is currently incompatible.
pushd $REDDIT_SRC
wget -nc https://launchpad.net/~reddit/+archive/ubuntu/ppa/+files/python-pycassa_1.11.0-1~trusty1reddit3_all.deb
apt-get install $APTITUDE_OPTIONS ./python-pycassa_1.11.0-1~trusty1reddit3_all.deb
popd

###############################################################################
# thrift
###############################################################################
#     sudo -u $REDDIT_USER git clone https://github.com/apache/thrift.git $REDDIT_SRC/thrift
#     pushd $REDDIT_SRC/thrift
#     sudo -u $REDDIT_USER git checkout v0.12.0
#     sudo -u $REDDIT_USER ./bootstrap.sh
#     sudo -u $REDDIT_USER ./configure
#     sudo -u $REDDIT_USER make
#     make install
#     cd lib/py
#     sudo -u $REDDIT_USER python setup.py build
#     python setup.py develop --no-deps
if ! type "thrift1" > /dev/null; then
    pushd $REDDIT_SRC

    # TODO: add Ubuntu 14 and 16 repos instead?
    # boost
    # add-apt-repository ppa:mhier/libboost-latest
    # apt update
    # apt install $APTITUDE_OPTIONS libboost1.54
    wget -nc http://archive.ubuntu.com/ubuntu/pool/main/i/icu/libicu52_52.1-3_amd64.deb
    wget -nc http://launchpadlibrarian.net/160798973/libboost-context1.54.0_1.54.0-4ubuntu3_amd64.deb
    wget -nc http://archive.ubuntu.com/ubuntu/pool/main/b/boost1.54/libboost-system1.54.0_1.54.0-4ubuntu3.1_amd64.deb
    wget -nc http://archive.ubuntu.com/ubuntu/pool/main/b/boost1.54/libboost-filesystem1.54.0_1.54.0-4ubuntu3.1_amd64.deb
    wget -nc http://archive.ubuntu.com/ubuntu/pool/main/b/boost1.54/libboost-program-options1.54.0_1.54.0-4ubuntu3.1_amd64.deb
    wget -nc http://archive.ubuntu.com/ubuntu/pool/main/b/boost1.54/libboost-regex1.54.0_1.54.0-4ubuntu3.1_amd64.deb
    wget -nc http://archive.ubuntu.com/ubuntu/pool/main/b/boost1.54/libboost-thread1.54.0_1.54.0-4ubuntu3.1_amd64.deb
    wget -nc http://archive.ubuntu.com/ubuntu/pool/main/libe/libevent/libevent-2.0-5_2.0.21-stable-2ubuntu0.16.04.1_amd64.deb
    wget -nc http://archive.ubuntu.com/ubuntu/pool/main/g/gflags/libgflags2_2.0-1.1ubuntu1_amd64.deb
    wget -nc http://launchpadlibrarian.net/138839004/libgoogle-glog0_0.3.3-1_amd64.deb
    wget -nc http://archive.ubuntu.com/ubuntu/pool/main/s/snappy/libsnappy1_1.1.0-1ubuntu1_amd64.deb

    apt-get install $APTITUDE_OPTIONS ./libicu52_52.1-3_amd64.deb
    apt-get install $APTITUDE_OPTIONS ./libboost-system1.54.0_1.54.0-4ubuntu3.1_amd64.deb
    apt-get install $APTITUDE_OPTIONS ./libboost-context1.54.0_1.54.0-4ubuntu3_amd64.deb
    apt-get install $APTITUDE_OPTIONS ./libboost-program-options1.54.0_1.54.0-4ubuntu3.1_amd64.deb
    apt-get install $APTITUDE_OPTIONS ./libboost-regex1.54.0_1.54.0-4ubuntu3.1_amd64.deb
    apt-get install $APTITUDE_OPTIONS ./libboost-thread1.54.0_1.54.0-4ubuntu3.1_amd64.deb
    apt-get install $APTITUDE_OPTIONS ./libevent-2.0-5_2.0.21-stable-2ubuntu0.16.04.1_amd64.deb
    apt-get install $APTITUDE_OPTIONS ./libgflags2_2.0-1.1ubuntu1_amd64.deb
    apt-get install $APTITUDE_OPTIONS ./libgoogle-glog0_0.3.3-1_amd64.deb
    apt-get install $APTITUDE_OPTIONS ./libsnappy1_1.1.0-1ubuntu1_amd64.deb

    # folly
    wget -nc https://launchpad.net/~reddit/+archive/ubuntu/ppa/+build/8320028/+files/libfolly55_0.55.0-0reddit1_amd64.deb
    apt-get install $APTITUDE_OPTIONS ./libfolly55_0.55.0-0reddit1_amd64.deb

    # yarpl
    # TODO PORT - this is wrong
    # git clone https://github.com/yschimke/reactive-streams-cpp
    # TODO - start over here
    # TODO - or bail and do the manual .debs!?!
    # git clone https://github.com/rsocket/rsocket-cpp.git

    # fbthrift
    # git clone https://github.com/facebook/fbthrift
    # cd fbthrift/build
    # cmake ..
    # make
    # sudo make install
    wget -nc https://launchpad.net/~reddit/+archive/ubuntu/ppa/+files/fbthrift-compiler_0.31.0-0reddit8_amd64.deb
    wget -nc https://launchpad.net/~reddit/+archive/ubuntu/ppa/+files/python-fbthrift_0.31.0-0reddit8_amd64.deb
    apt-get install $APTITUDE_OPTIONS ./fbthrift-compiler_0.31.0-0reddit8_amd64.deb
    apt-get install $APTITUDE_OPTIONS ./python-fbthrift_0.31.0-0reddit8_amd64.deb
    popd
fi

###############################################################################
# baseplate - required by reddit-service-activity
###############################################################################
if ! type "baseplate-serve2" > /dev/null; then
    pushd $REDDIT_SRC
    # TODO PORT
    # sudo -u $REDDIT_USER git clone https://github.com/reddit/baseplate.git $REDDIT_SRC/baseplate
    # sudo -u $REDDIT_USER git checkout v0.28.6
    # sudo -u $REDDIT_USER make
    # sudo -u $REDDIT_USER python setup.py build
    # python setup.py develop --no-deps
    wget -nc https://launchpad.net/~reddit/+archive/ubuntu/ppa/+files/python-baseplate_0.28.6_amd64.deb
    apt-get install $APTITUDE_OPTIONS ./python-baseplate_0.28.6_amd64.deb
    popd
fi