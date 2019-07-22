#!/bin/bash
# Creates date-saidit-backup.tar.gz, and removes any prior backups. Run as root!
# Cron job: 20 4 * * * root /home/reddit/src/reddit/scripts/saidit-backup.sh
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

# cassandra
nodetool clearsnapshot
nodetool flush
nodetool snapshot
mkdir $BKUPPATH/temp/cassandra
cp -r /var/lib/cassandra/data/reddit "$BKUPPATH"/temp/cassandra

# media
rm -rf $BKUPPATH/temp/media
cp -r /srv/www/media $BKUPPATH/temp

# app
cp /etc/cron.d/reddit $BKUPPATH/temp/crond-reddit
cp /etc/default/reddit $BKUPPATH/temp/etc-default-reddit.conf
cp $HOMEPATH/src/reddit/r2/development.update $BKUPPATH/temp/development.update
cp $HOMEPATH/src/reddit/r2/development2.ini $BKUPPATH/temp/development2.ini
cp $HOMEPATH/src/reddit/r2/development3.ini $BKUPPATH/temp/development3.ini
cp $HOMEPATH/src/reddit/r2/development4.ini $BKUPPATH/temp/development4.ini
cp $HOMEPATH/src/reddit/r2/development4.ini $BKUPPATH/temp/development5.ini
cp $HOMEPATH/src/reddit/r2/development4.ini $BKUPPATH/temp/development6.ini
cp /etc/init/reddit-paster.conf $BKUPPATH/temp/reddit-paster.conf
cp /etc/init/reddit-paster2.conf $BKUPPATH/temp/reddit-paster2.conf
cp /etc/init/reddit-paster3.conf $BKUPPATH/temp/reddit-paster3.conf
cp /etc/init/reddit-paster4.conf $BKUPPATH/temp/reddit-paster4.conf
cp /etc/init/reddit-paster5.conf $BKUPPATH/temp/reddit-paster5.conf
cp /etc/init/reddit-paster6.conf $BKUPPATH/temp/reddit-paster6.conf

# app dependencies
cp /etc/memcached.conf $BKUPPATH/temp/memcached.conf
cp /etc/cassandra/cassandra-env.sh $BKUPPATH/temp/cassandra-env.sh
cp /etc/tomcat7/server.xml $BKUPPATH/temp/tomcat-server.conf
cp /etc/postfix/main.cf $BKUPPATH/temp/postfix-main.cf
cp /etc/nginx/conf.d/reddit.conf $BKUPPATH/temp/reddit.conf
cp /etc/nginx/sites-available/reddit-ssl $BKUPPATH/temp/reddit-ssl
cp /etc/nginx/sites-available/reddit-media $BKUPPATH/temp/reddit-media
cp /etc/nginx/sites-available/reddit-pixel $BKUPPATH/temp/reddit-pixel

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