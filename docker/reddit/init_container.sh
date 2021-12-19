#!/bin/bash

# rsyslog
rsyslogd

# cron
cron -L15

# cassandra
while ! nc -vz $CASSANDRA_HOST $CASSANDRA_PORT; do
    echo "Waiting for Cassandra..."
    sleep 1
done
./init_cassandra.sh

# postgres
while ! nc -vz $POSTGRES_HOST $POSTGRES_PORT; do
    echo "Waiting for Postgres..."
    sleep 1
done

# rabbitmq
while ! nc -vz $RABBITMQ_HOST $RABBITMQ_PORT; do
    echo "Waiting for RabbitMQ..."
    sleep 1
done

# supervisord is the main docker foreground process
/usr/bin/supervisord -n