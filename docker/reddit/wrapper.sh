#!/bin/bash

# exit immediately if a command exits with a non-zero status
set -e

# init stuff
. /etc/default/reddit
# ./init_cassandra.sh
echo path is $PATH
echo reddit root $REDDIT_ROOT
echo reddit src $REDDIT_SRC
alias

# upstart/reddit-paster.conf
$REDDIT_SRC/reddit/scripts/wrap-job paster serve --reload $REDDIT_INI &
# gunicorn_paster --log-file=/var/log/syslog $REDDIT_INI
  
# Wait for any process to exit
wait -n
  
# Exit with status of process that exited first
exit $?