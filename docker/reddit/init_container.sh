#!/bin/bash

# cassandra
while ! nc -vz $CASSANDRA_HOST $CASSANDRA_PORT; do
    echo "Waiting for Cassandra..."
    sleep 1
done
./init_cassandra.sh

# postgres
# until pg_isready --username=$POSTGRES_USER --host=$POSTGRES_HOST; do sleep 1; done
while ! nc -vz $POSTGRES_HOST $POSTGRES_PORT; do
    echo "Waiting for Postgres..."
    sleep 1
done

# supervisord is the main docker foreground process
/usr/bin/supervisord -n