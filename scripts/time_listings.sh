#!/bin/bash

# SAIDIT: run sequentially and sleep for max single server performance
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null 2>&1 && pwd )"
/bin/bash $DIR/compute_time_listings link year "['hour', 'day', 'week', 'month', 'year']" 2>&1 | /usr/bin/logger -t compute_time_listings_link
sleep 10
/bin/bash $DIR/compute_time_listings comment year "['hour', 'day', 'week', 'month', 'year']" 2>&1 | /usr/bin/logger -t compute_time_listings_comment