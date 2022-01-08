#!/bin/bash

# start rsyslog service
rsyslogd

# supervisord is the main docker foreground process
/usr/bin/supervisord -n