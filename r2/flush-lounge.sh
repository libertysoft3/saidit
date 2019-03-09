#!/bin/bash

kill $(pgrep -f "node index");
rm -f /home/reddit/.lounge/users/*;
rm -rf /home/reddit/.lounge/storage;
cd /home/reddit/lounge-autoconnect;
yes N | node index add first-user;
nohup npm start ./ >> thelounge.log 2>&1 &
exit
