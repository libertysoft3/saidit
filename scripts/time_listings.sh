#!/bin/bash

# SAIDIT: running sequentially for single server performance
# see also WRITE_PERMACACHE_NPROC, WRITE_PERMACACHE_SLEEP
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null 2>&1 && pwd )"

/bin/bash $DIR/compute_time_listings link year "['year']" 2>&1 | /usr/bin/logger -t compute_time_listings_link
/bin/bash $DIR/compute_time_listings link month "['month']" 2>&1 | /usr/bin/logger -t compute_time_listings_link
/bin/bash $DIR/compute_time_listings link week "['week']" 2>&1 | /usr/bin/logger -t compute_time_listings_link
/bin/bash $DIR/compute_time_listings link day "['day']" 2>&1 | /usr/bin/logger -t compute_time_listings_link
/bin/bash $DIR/compute_time_listings link hour "['hour']" 2>&1 | /usr/bin/logger -t compute_time_listings_link

/bin/bash $DIR/compute_time_listings comment year "['year']" 2>&1 | /usr/bin/logger -t compute_time_listings_comment
/bin/bash $DIR/compute_time_listings comment month "['month']" 2>&1 | /usr/bin/logger -t compute_time_listings_comment
/bin/bash $DIR/compute_time_listings comment week "['week']" 2>&1 | /usr/bin/logger -t compute_time_listings_comment
/bin/bash $DIR/compute_time_listings comment day "['day']" 2>&1 | /usr/bin/logger -t compute_time_listings_comment
/bin/bash $DIR/compute_time_listings comment hour "['hour']" 2>&1 | /usr/bin/logger -t compute_time_listings_comment
