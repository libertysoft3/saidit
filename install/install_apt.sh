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

# facebook mcrouter repo
echo deb https://facebook.github.io/mcrouter/debrepo/bionic bionic contrib | \
    sudo tee $MCROUTER_SOURCES_LIST

wget -qO- -L https://facebook.github.io/mcrouter/debrepo/bionic/PUBLIC.KEY | \
    sudo apt-key add -

# run an aptitude update to make sure python-software-properties
# dependencies are found
apt-get update
apt-get -y upgrade

# add the reddit ppa for some custom packages
# apt-get install $APTITUDE_OPTIONS python-software-properties
# apt-add-repository -y ppa:reddit/ppa

# pin the ppa -- packages present in the ppa will take precedence over
# ones in other repositories (unless further pinning is done)
# cat <<HERE > /etc/apt/preferences.d/reddit
# Package: *
# Pin: release o=LP-PPA-reddit
# Pin-Priority: 600
# HERE

# grab the new ppas' package listings
# apt-get update

# travis gives us a stock libmemcached.  We have to remove that
# apt-get remove $APTITUDE_OPTIONS $(dpkg-query  -W -f='${binary:Package}\n' | grep libmemcached | tr '\n' ' ')
# apt-get autoremove $APTITUDE_OPTIONS

# install prerequisites
cat <<PACKAGES | xargs apt-get install $APTITUDE_OPTIONS
libssl1.0-dev
build-essential
python
python-dev
python-setuptools
cmake
flex
libmstch-dev
libzstd-dev
zlib1g-dev
libgflags2.2
libgflags-dev
libgoogle-glog-dev
libsnappy-dev
python-snappy
libsodium-dev
libdouble-conversion-dev
libevent-dev
libtool
ragel
gettext
PACKAGES

# bison
cat <<PACKAGES | xargs apt-get install $APTITUDE_OPTIONS
autoconf
autopoint
texinfo
help2man
PACKAGES

# folly
cat <<PACKAGES | xargs apt-get install $APTITUDE_OPTIONS
libboost-dev
libboost-filesystem-dev
libboost-thread-dev
libboost-context-dev
libboost-program-options-dev
libboost-regex-dev
libboost-python-dev
PACKAGES

# baseplate
cat <<PACKAGES | xargs apt-get install $APTITUDE_OPTIONS
python-jwt
python-posix-ipc
python-gevent
python-future
python-typing
python-concurrent.futures
PACKAGES

# reddit
cat <<PACKAGES | xargs apt-get install $APTITUDE_OPTIONS
cython
gperf
python-psycopg2
python-contextlib2
python-kazoo
python-pil
PACKAGES

