# saidit

[saidit.net](https://saidit.net) is a [reddit](https://github.com/reddit-archive/reddit) fork which also uses:

* forked [TheLounge web IRC client](https://github.com/libertysoft3/lounge-autoconnect)
* custom [snudown](https://github.com/libertysoft3/snudown)
* optional custom [Reddit Enhancement Suite](https://github.com/libertysoft3/Reddit-Enhancement-Suite)

saidit changes:

* bug fixes
* rebranding system
* custom voting/score model: insightful is +2, funny is +1
* custom admin tools

additional documentation:

* [https://github.com/reddit-archive/reddit/wiki](https://github.com/reddit-archive/reddit/wiki)
* [https://www.reddit.com/r/RedditOpenSource](https://www.reddit.com/r/RedditOpenSource)
* [https://www.reddit.com/r/redditdev](https://www.reddit.com/r/redditdev)

---

## installation

This guide will walk you through installing reddit on a [VirtualBox](https://www.virtualbox.org/wiki/Downloads) virtual machine. This can be done on Linux, Mac, or Windows. 

If you prefer you can install directly on a VPS running [Ubuntu 14](http://releases.ubuntu.com/14.04/) (create user "reddit" with sudo privileges and skip to "install reddit"). Also an ip address can be used in place of "reddit.local".


### create a Ubuntu 14.04 VM with VirtualBox

1. Download Ubuntu 14.04 server edition
1. In VirtualBox, after creating a new VM with 4gb RAM and 30gb disk space, 
1. Set networking to use a "Bridged Adapter"
1. Add a CD rom entry and select the Ubuntu 14 .iso
1. Boot the VM
1. In the Ubuntu installer:
  1. Choose username "reddit"
  1. Choose to install "OpenSSH Server"
  1. Complete Ubuntu installation. 
1. Login and run `ifconfig` and note your ip address
1. If you forgot to install the openssh server, run `sudo apt-get install openssh-server`
1. You can now detach your VM or shut it down and restart in headless mode. You should only interact with it via SSH from your host for easy copy and paste, etc. Don't forget to shut down your VM before shutting down the host OS or you may corrupt your reddit installation.

### update your (host's) hosts file to resolve https://reddit.local in your browser

Add the ip you noted earlier to your hosts file as "reddit.local". This procedure [varies by OS](https://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/). Once this is setup you can ssh into your VM easily with `ssh reddit@reddit.local`

### install reddit

login to your VM as user reddit with `ssh reddit@reddit.local`. first we will update the OS.

    # WARNING: Never run an apt-get "do-release-upgrade" or you will upgrade Ubuntu and break reddit
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install git

reddit installation

    cd ~/
    git clone https://github.com/libertysoft3/reddit-ae.git
    chmod +x reddit/install-reddit.sh
    sudo ./reddit/install/reddit.sh
    # if you get an error about "less" restart the server and try again
    # reddit has been installed at ~/src/reddit.
    rm -rf reddit

optional: install sample data (recommended for demo/development enviroments)

    cd ~/src/reddit
    reddit-run scripts/inject_test_data.py -c 'inject_test_data()'
    sudo start reddit-job-update_popular_subreddits
    # NOTE: an admin user "reddit" with password "password" is created


### additional configuration

make reddit user "cloner" a reddit admin

    # Create reddit account "cloner" in your host's browser at https://reddit.local before or after this config change
    cd ~/src/reddit/r2
    nano development.update
    # edit: employees = reddit:admin
    # to: employees = reddit:admin, cloner:admin
    # because configuration has changed run
    make ini
    sudo reddit-flush
    # Logged in as "cloner" you should now see the "turn admin on" link

increase PostgreSQL max_connections for greater stability (87/100 in use at reddit idle without Solr running?)

    sudo nano /etc/postgresql/9.3/main/postgresql.conf
    # edit: max_connections = 100
    # to: max_connections = 150
    sudo service postgresql restart
    sudo reddit-restart

add some missing cron jobs to `/etc/cron.d/reddit`

    15 * * * * root /sbin/start reddit-job-update_popular_subreddits
    20 * * * * root /sbin/start reddit-job-hourly_traffic
    15 3 * * * root /sbin/start reddit-job-subscribers
    */5  * * * * root /sbin/start reddit-job-update_trending_subreddits

optional: change the default subreddits that guests see

    cd ~/src/reddit/r2
    paster shell run.ini
    # paste the following, hit enter:
    from r2.models import *
    srs = [Subreddit._by_name(n) for n in ("pics", "videos", "science", "technology")]
    LocalizedDefaultSubreddits.set_global_srs(srs)
    LocalizedFeaturedSubreddits.set_global_srs([Subreddit._by_name('pics')])
    exit()

watch reddit run and debug errors

    sudo tail -f /var/log/syslog

### optional: accessing VM files from your host

You can mount the VM's reddit files as a folder on your host machine for easy editing and searching. sshfs is a quick and easy approach. On your host install sshfs and run `sshfs reddit@reddit.local:/home/reddit/src/reddit ~/vm`. Unmount it later with `fusermount -u ~/vm` to avoid crashing your editor when your VM shuts down.

---

## Ubuntu 14 updates
 
### update OS
 
    $ sudo apt-get update
    $ sudo apt-get upgrade


### upgrade curl

this will improve reddit's 'fetch title' functionality and potentially more.
 
    replace version with latest stable from https://curl.haxx.se/download.html:
    $ sudo apt-get build-dep curl
    $ wget http://curl.haxx.se/download/curl-7.58.0.tar.bz2
    $ tar -xvjf curl-7.58.0.tar.bz2
    $ cd curl-7.58.0
    $ ./configure --prefix=/usr
    $ make
    $ sudo make install
    $ sudo ldconfig
    $ curl --version
 
 
### upgrade python from 2.7.6 to 2.7.14

[source](https://askubuntu.com/a/725173)
 
    $ sudo add-apt-repository ppa:jonathonf/python-2.7
    $ sudo apt-get update
    $ sudo apt-get install python2.7
    $ python --version


### rebuild reddit from source
 
    $ sudo reddit-stop
    $ sudo-reddit-flush
    $ sudo apt-get install libxml2-dev libxslt1-dev python-dev
    $ cd ~/src/reddit/r2
    $ python setup.py build
    $ sudo python setup.py develop
    $ make clean
    $ make
    $ sudo reddit-start

---

## solr search
 
### install Solr

As user "reddit" run:

    cd ~
    sudo apt-get install tomcat7 tomcat7-admin software-properties-common
    # installs java, openjdk-7-jre-headless
    wget http://archive.apache.org/dist/lucene/solr/4.10.4/solr-4.10.4.tgz
    tar -xvzf solr-4.10.4.tgz
    sudo mv solr-4.10.4 /usr/share/solr
    sudo chown -R tomcat7:tomcat7 /usr/share/solr/example
 
    # Setup Solr, install Reddit schema
    sudo cp /usr/share/solr/example/webapps/solr.war /usr/share/solr/example/solr/
    sudo cp /usr/share/solr/example/lib/ext/* /usr/share/tomcat7/lib/
    sudo cp /usr/share/solr/example/resources/log4j.properties /usr/share/tomcat7/lib/
 
    sudo mv /usr/share/solr/example/solr/collection1/conf/schema.xml /usr/share/solr/example/solr/collection1/conf/schema.xml.bak
    sudo cp src/reddit/solr/schema4.xml /usr/share/solr/example/solr/collection1/conf/schema.xml
    sudo chown tomcat7:tomcat7 /usr/share/solr/example/solr/collection1/conf/schema.xml
 
    # Setup Tomcat for Solr
    sudo nano /usr/share/tomcat7/lib/log4j.properties
    # edit to set:
    solr.log=/usr/share/solr
 
    sudo nano /etc/tomcat7/Catalina/localhost/solr.xml
    # add content:
    <Context docBase="/usr/share/solr/example/solr/solr.war" debug="0" crossContext="true">
      <Environment name="solr/home" type="java.lang.String" value="/usr/share/solr/example/solr" override="true" />
    </Context>
 
    # have tomcat use port 8983, 8080 is taken by haproxy
    sudo nano /etc/tomcat7/server.xml
    # edit to set:
    <Connector port="8983" protocol="HTTP/1.1"
 
    # Solr is missing some required stuff:
    sudo touch /usr/share/solr/solr.log
    sudo mkdir /usr/share/tomcat7/temp
    sudo chown tomcat7:tomcat7 /usr/share/solr/solr.log
    sudo chown tomcat7:tomcat7 /usr/share/tomcat7/temp
 
    # verify tomcat all good (ignore warnings):
    /usr/share/tomcat7/bin/configtest.sh
 
    sudo service tomcat7 restart
 
    # any errors in here must be fixed
    sudo cat /var/log/tomcat7/catalina.out
 
    # verify working, these should return html pages:
    wget 127.0.0.1:8983
    wget 127.0.0.1:8983/solr
 
### configure reddit to use Solr for search:
 
    # as non-root user
    nano ~/src/reddit/r2/development.update
    # NOTE: solr port changed from default 8080 to 8983
    search_provider = solr
    solr_version = 4
    solr_search_host = 127.0.0.1
    solr_doc_host = 127.0.0.1
    solr_subreddit_search_host = 127.0.0.1
    solr_subreddit_doc_host = 127.0.0.1
    solr_port = 8983
    solr_core = collection1
    solr_min_batch = 500
    solr_query_parser =
 
    # since config has changed:
    cd ~/src/reddit/r2
    make ini
    sudo reddit-restart
 
### add reddit content to Solr, verify working:

    cd ~/src/reddit/r2
    paster run run.ini -c 'import r2.lib.providers.search.solr as cs; cs.rebuild_subreddit_index()'
    paster run run.ini -c 'import r2.lib.providers.search.solr as cs; cs._rebuild_link_index()'
 
 
### setup Solr cron jobs:
 
    sudo nano /etc/init/reddit-job-solr_subreddits.conf
    # paste lines, save:
    description "Add new subreddits to Solr."
    manual
    task
    stop on reddit-stop or runlevel [016]
    nice 10
    script
        . /etc/default/reddit
        wrap-job paster run $REDDIT_INI -c 'import r2.lib.providers.search.solr as cs; cs.rebuild_subreddit_index()'
    end script
 
and then...
 
    sudo nano /etc/init/reddit-job-solr_links.conf
    # paste lines, save:
    description "Add new posts to Solr."
    manual
    task
    stop on reddit-stop or runlevel [016]
    nice 10
    script
        . /etc/default/reddit
        wrap-job paster run $REDDIT_INI -c 'import r2.lib.providers.search.solr as cs; cs._rebuild_link_index()'
    end script
 
and then...
 
    echo '# Solr search:' | sudo tee --append /etc/cron.d/reddit
    echo '*/3  * * * * root /sbin/start --quiet reddit-job-solr_subreddits' | sudo tee --append /etc/cron.d/reddit
    echo '* * * * * root /sbin/start --quiet reddit-job-solr_links' | sudo tee --append /etc/cron.d/reddit
