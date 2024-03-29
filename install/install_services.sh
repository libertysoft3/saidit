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

###############################################################################
# Install services
###############################################################################

# load configuration
RUNDIR=$(dirname $0)
source $RUNDIR/install.cfg

# install prerequisites
if [ "$INSTALL_PROFILE" = "all" ]; then
    cat <<PACKAGES | xargs apt-get install $APTITUDE_OPTIONS
mcrouter
memcached
postgresql
postgresql-client
rabbitmq-server
haproxy
nginx
redis-server
gunicorn
PACKAGES

elif [ "$INSTALL_PROFILE" = "docker" ]; then
    cat <<PACKAGES | xargs apt-get install $APTITUDE_OPTIONS
postgresql-client
redis-server
gunicorn
nginx
PACKAGES

fi

###############################################################################
# Wait for all the services to be up
###############################################################################
# check each port for connectivity
echo "Waiting for services to be available, see source for port meanings..."
# 11211 - memcache, 5432 - postgres, 5672 - rabbitmq
if [ "$INSTALL_PROFILE" = "all" ]; then
    for port in 11211 5432 5672; do
        while ! nc -vz localhost $port; do
            sleep 1
        done
    done
fi