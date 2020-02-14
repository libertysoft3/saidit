#!/bin/bash
#
# SaidIt: running sequentially for single server performance
start=$(date +%s.%N)
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null 2>&1 && pwd )"

/bin/bash $DIR/compute_time_listings link year "['hour', 'day', 'week', 'month', 'year']" 2>&1 | /usr/bin/logger -t compute_time_listings_link
/bin/bash $DIR/compute_time_listings comment year "['hour', 'day', 'week', 'month', 'year']" 2>&1 | /usr/bin/logger -t compute_time_listings_comment

duration=$(echo "$(date +%s.%N) - $start" | bc)
execution_time=`printf "%.2f seconds" $duration`
echo "Done, links and comments took $execution_time." | /usr/bin/logger -t compute_time_listings