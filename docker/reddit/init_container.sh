#!/bin/bash

# start rsyslog service
rsyslogd

# wait for cassandra
while ! nc -vz $CASSANDRA_HOST $CASSANDRA_PORT; do
    echo "Waiting for Cassandra..."
    sleep 1
done

# init cassandra
python <<END
import pycassa
sys = pycassa.SystemManager("$CASSANDRA_HOST:$CASSANDRA_PORT")

if "reddit" not in sys.list_keyspaces():
    print "creating keyspace 'reddit'"
    sys.create_keyspace("reddit", "SimpleStrategy", {"replication_factor": "1"})
    print "done"

if "permacache" not in sys.get_keyspace_column_families("reddit"):
    print "creating column family 'permacache'"
    sys.create_column_family("reddit", "permacache")
    print "done"
END

# wait for postgres
while ! nc -vz $POSTGRES_HOST $POSTGRES_PORT; do
    echo "Waiting for Postgres..."
    sleep 1
done

# wait for rabbitmq
while ! nc -vz $RABBITMQ_HOST $RABBITMQ_PORT; do
    echo "Waiting for RabbitMQ..."
    sleep 1
done

# init reddit app
REDDIT_INIT_ONCE="/home/reddit/install-complete"
if [ ! -e $REDDIT_INIT_ONCE ]; then
    echo "Initializing reddit with inject_configuration_data()..."
    touch $REDDIT_INIT_ONCE
    reddit-run $REDDIT_HOME/src/reddit/scripts/inject_test_data.py -c 'inject_configuration_data()'
fi

# start cron service
cron

# supervisord is the main docker foreground process
/usr/bin/supervisord -n