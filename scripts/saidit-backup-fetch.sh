#!/bin/bash
# Downloads your saidit backups
# Cron job: 20 5 * * * you /home/you/saidit-backups/saidit-backup.sh
# Ref: https://unix.stackexchange.com/a/127355

# Create a SSH key and add it to the server:
# $ ssh-keygen -t rsa -b 4096 -C "you" -f ~/.ssh/id_rsa_saidit
# $ cat ~/.ssh/id_rsa_saidit.pub | ssh reddit@reddit.local 'cat >> ~/.ssh/authorized_keys'

mkdir -p ~/saidit-backups
rsync -htP -e "ssh -i ~/.ssh/id_rsa_saidit" reddit@reddit.local:/home/reddit/backup/*saidit-backup.tar.gz ~/saidit-backups