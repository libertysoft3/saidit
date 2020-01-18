#!/bin/bash
# SAIDIT: making these run sequentially for performance
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null 2>&1 && pwd )"
/bin/bash $DIR/compute_time_listings link year "['hour', 'day', 'week', 'month', 'year']" 2>&1 | /usr/bin/logger -t compute_time_listings_link
/bin/bash $DIR/compute_time_listings comment year "['hour', 'day', 'week', 'month', 'year']" 2>&1 | /usr/bin/logger -t compute_time_listings_comment