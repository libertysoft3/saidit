#!/bin/bash

# from setup_cassandra.sh
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