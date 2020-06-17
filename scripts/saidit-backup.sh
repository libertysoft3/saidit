#!/bin/bash
# Creates date-saidit-backup.tar.gz, and removes any prior backups. Run as root!
# Cron job: 20 4 * * * root /home/reddit/src/reddit/scripts/saidit-backup.sh
# media at /srv/www/media is not included, using rsync
HOMEPATH=/home/reddit
BKUPPATH=$HOMEPATH/backup
CHOWNTOUSER=reddit
POSTGRESUSER=reddit

# init
mkdir -p $BKUPPATH
mkdir -p $BKUPPATH/temp
rm -rf $BKUPPATH/temp/*
chown -R $CHOWNTOUSER:$CHOWNTOUSER $BKUPPATH

# postgres
sudo -u $POSTGRESUSER pg_dump -U $POSTGRESUSER reddit > $BKUPPATH/temp/reddit.sql
cp /etc/postgresql/9.3/main/postgresql.conf $BKUPPATH/temp/postgresql.conf

# cassandra
nodetool clearsnapshot
nodetool flush
nodetool snapshot
mkdir $BKUPPATH/temp/cassandra
cp -r /var/lib/cassandra/data/reddit "$BKUPPATH"/temp/cassandra

# app
cp /etc/cron.d/reddit $BKUPPATH/temp/crond-reddit
cp /etc/default/reddit $BKUPPATH/temp/etc-default-reddit.conf
cp $HOMEPATH/src/reddit/r2/development.update $BKUPPATH/temp/development.update
cp /etc/init/reddit-paster.conf $BKUPPATH/temp/reddit-paster.conf

# services
cp /etc/memcached.conf $BKUPPATH/temp/memcached.conf
cp /etc/cassandra/cassandra-env.sh $BKUPPATH/temp/cassandra-env.sh
cp /etc/tomcat7/server.xml $BKUPPATH/temp/tomcat-server.conf
cp /etc/postfix/main.cf $BKUPPATH/temp/postfix-main.cf
cp /etc/nginx/nginx.conf $BKUPPATH/temp/nginx.conf
cp /etc/nginx/conf.d/reddit.conf $BKUPPATH/temp/reddit.conf
cp /etc/nginx/sites-available/reddit-ssl $BKUPPATH/temp/reddit-ssl
cp /etc/nginx/sites-available/reddit-media $BKUPPATH/temp/reddit-media
cp /etc/nginx/sites-available/reddit-pixel $BKUPPATH/temp/reddit-pixel
cp /etc/haproxy/haproxy.cfg $BKUPPATH/temp/haproxy.cfg
cp /etc/default/mcrouter $BKUPPATH/temp/mcrouter
cp /etc/mcrouter/global.conf $BKUPPATH/temp/mcrouter-global.conf

# ssl cert
cp /etc/letsencrypt/live/saidit.net/fullchain.pem $BKUPPATH/temp/fullchain.pem
cp /etc/letsencrypt/live/saidit.net/privkey.pem $BKUPPATH/temp/privkey.pem

# chat
cp $HOMEPATH/.lounge/config.js $BKUPPATH/temp/lounge-config.js
cp $HOMEPATH/unrealircd/conf/unrealircd.conf $BKUPPATH/temp/unrealircd.conf
cp $HOMEPATH/unrealircd/conf/ircd.motd $BKUPPATH/temp/ircd.motd
cp $HOMEPATH/services/conf/services.conf $BKUPPATH/temp/services.conf

# OS
cp /etc/fail2ban/jail.local $BKUPPATH/temp/jail.local
iptables-save > $BKUPPATH/temp/iptables-export
cp /etc/security/limits.conf $BKUPPATH/temp/limits.conf
cp /etc/sysctl.conf $BKUPPATH/temp/sysctl.conf

# finish
chown -R $CHOWNTOUSER $BKUPPATH/temp
rm -f $BKUPPATH/*saidit-backup.tar.gz
tar -zcf $BKUPPATH/`date +\%Y\%m\%d`-saidit-backup.tar.gz -C $BKUPPATH/temp .
chown $CHOWNTOUSER:$CHOWNTOUSER $BKUPPATH/`date +\%Y\%m\%d`-saidit-backup.tar.gz
rm -rf $BKUPPATH/temp
