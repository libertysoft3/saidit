#!/bin/bash

# exit immediately if a command exits with a non-zero status
set -e

# from setup_cassandra.sh, can't run until 2 containers are running
python <<END
import pycassa
sys = pycassa.SystemManager("cassandra:9160")

if "reddit" not in sys.list_keyspaces():
    print "creating keyspace 'reddit'"
    sys.create_keyspace("reddit", "SimpleStrategy", {"replication_factor": "1"})
    print "done"

if "permacache" not in sys.get_keyspace_column_families("reddit"):
    print "creating column family 'permacache'"
    sys.create_column_family("reddit", "permacache")
    print "done"
END
