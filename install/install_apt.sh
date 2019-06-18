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

# run an aptitude update to make sure software-properties-common
# dependencies are found
apt-get update

# add the datastax cassandra repos (NB: this is required for
# install_cassandra.sh to work correctly, and the non-existence of this
# file will trigger install_cassandra.sh to rerun this script)
echo deb http://debian.datastax.com/community stable main | \
    sudo tee $CASSANDRA_SOURCES_LIST
    
wget -qO- -L https://debian.datastax.com/debian/repo_key | \
    sudo apt-key add -

echo deb https://facebook.github.io/mcrouter/debrepo/bionic bionic contrib | \
    sudo tee $FACEBOOK_SOURCES_LIST

wget -qO- -L https://facebook.github.io/mcrouter/debrepo/xenial/PUBLIC.KEY | \
    sudo apt-key add -

# add the reddit ppa for some custom packages
apt-get install $APTITUDE_OPTIONS software-properties-common

# TODO - try to move away from this
# apt-add-repository -y ppa:reddit/ppa

# pin the ppa -- packages present in the ppa will take precedence over
# ones in other repositories (unless further pinning is done)
# cat <<HERE > /etc/apt/preferences.d/reddit
# Package: *
# Pin: release o=LP-PPA-reddit
# Pin-Priority: 600
# HERE

# grab the new ppas' package listings
apt-get update

# travis gives us a stock libmemcached.  We have to remove that
apt-get remove $APTITUDE_OPTIONS $(dpkg-query  -W -f='${binary:Package}\n' | grep libmemcached | tr '\n' ' ')
apt-get autoremove $APTITUDE_OPTIONS

# TODO - removing python-pylibmc=1.2.2-1~trusty5 too ????
# install prerequisites
cat <<PACKAGES | xargs apt-get install $APTITUDE_OPTIONS
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
python-babel
python-numpy
python-dateutil
cython
python-sqlalchemy
python-beautifulsoup
python-chardet
python-psycopg2
python-pycassa
python-pil
python-pylibmc
python-amqplib
python-bcrypt
python-snappy

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
flex
bison
libboost-all-dev

g++
cmake
make
automake
pkg-config
libboost-all-dev
libevent-dev
libdouble-conversion-dev
libgoogle-glog-dev
libgflags-dev
libiberty-dev
liblz4-dev
liblzma-dev
libsnappy-dev
zlib1g-dev
binutils-dev
libjemalloc-dev
libzstd-dev
libffi-dev
python-cffi

mcrouter
PACKAGES
