# SaidIt

![Image of Saidit logo](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTWA5A1rZZJu_oFjSkUk42Ds5-UDm6c9HNkwSngMYAtvc_Dybkt)



SaidIt is a [reddit open source](https://github.com/reddit-archive/reddit) continuation and fork with:

* critical configurations restored
* critical bug fixes
* admin user bans and ip bans
* configurable site branding
* configurable home page
* enhanced expandos/embeds: more media providers, direct media links, used in comments, sidebars and wiki pages

SaidIt customizations include:

* two dimensional voting where insightful is +2 and fun is +1
* public moderator logs
* chat integration with a custom [TheLounge](https://github.com/libertysoft3/lounge-autoconnect) web IRC client

Goals:

* easily setup your own saidit/reddit open source clone
* platform upgrades, longevity
* enhancements and quality of life improvements
* reddit API compatibility

---

## Installation

There are two ways to set up a saidit server: on a standalone physical server, or through a Virtual Machine environment (running within another OS such as linux, MacOS, or Windows) for development and testing purposes.

### Setting up a virtual machine

1. Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
1. Download the latest [Ubuntu 14.04](http://releases.ubuntu.com/14.04/) server .iso file "64-bit PC (AMD64) server install image"
1. Start VirtualBox and click 'New'
   1. Type: Linux
   1. Version: Ubuntu (64-bit)
   1. Memory Size: 4000 MB (minimum)
   1. File location and size: 30.0 GB (minimim)
1. Right click the new VM and choose 'Settings'
   1. Network: Adapter 1: Attached to: "Bridged Adapter"
   1. Storage: select the empty CD icon and click "Choose Virtual Optical Disk File" and choose the ubuntu server .iso file
1. Select the new VM and click 'Start'
1. Install Ubuntu and choose following options, but leaving all other options with the default selection:
   1. Username: reddit
   1. Choose software to install: select OpenSSH, but no others
1. Complete Ubuntu installation

From this point forward you can start your VM with Start -> Headless Start and connect via ssh as user 'reddit' if you wish, using a program like [PuTTY](https://www.putty.org/). Don't forget to shut down your VM by right clicking it and choosing Close -> ACPI Shutdown before shutting down your host OS or you may corrupt your VM.

### Setting up a physical server

1. Download the latest [Ubuntu 14.04](http://releases.ubuntu.com/14.04/) server .ISO file "64-bit PC (AMD64) server install image"
1. Download [Rufus](https://rufus.ie/) (as recommended by Ubuntu) and use it to write the .ISO to a USB drive
1. Once finished, put the USB drive in the server and boot to it
1. Install Ubuntu with the following options, but leaving all other options with the default selection:
   1. Username: reddit
   1. Choose software to install: select OpenSSH, but no others
1. When install finishes, remove USB drive and boot to linux

From this point forward physical access to the server is no longer needed and you can ssh in as the 'reddit' user remotely if you wish, using a program like [PuTTY](https://www.putty.org/).


### Configure DNS for reddit.local

To use your reddit server, you are expected to be able to resolve reddit.local and https://reddit.local. First, find the ip address of your saidit server by running:

    $ ifconfig
    # note the 'inet addr' for device 'eth0' or similar

Then update your `hosts` file on your development machine/host OS. For example, on linux with saidit server ip 192.168.1.20  run:

    $ sudo sed -i '1i 192.168.1.20 reddit.local' /etc/hosts

For Windows and MacOS see https://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/


### Install SaidIt

SSH into your saidit server

    $ ssh reddit@reddit.local

Install SaidIt

    $ wget https://raw.github.com/libertysoft3/saidit/master/install-reddit.sh
    $ chmod +x install-reddit.sh
    $ sudo ./install-reddit.sh

You should see success message "Congratulations! reddit is now installed." Do not proceed if the installation failed with an error.

Visit https://reddit.local and create accounts for users 'reddit' and 'automoderator'. Alternatively, you can install some default/sample data including users 'reddit' and 'automoderator' (with password 'password'), subs, posts, and comments with:

    $ reddit-run ~/src/reddit/scripts/inject_test_data.py -c 'inject_test_data()'

SaidIt is now fully functional aside from search and optional chat. The [SaidIt Admin Guide](https://github.com/libertysoft3/saidit/wiki/Admin-guide) has instructions for changing your site configuration.

---

## Install search

SaidIt comes pre-configured for Solr search, but Solr and Tomcat are not installed yet.
 
Install Solr

    $ cd ~
    $ sudo apt-get install tomcat7 tomcat7-admin software-properties-common
    $ wget http://archive.apache.org/dist/lucene/solr/4.10.4/solr-4.10.4.tgz
    $ tar -xvzf solr-4.10.4.tgz
    $ sudo mv solr-4.10.4 /usr/share/solr
    $ sudo chown -R tomcat7:tomcat7 /usr/share/solr/example
 
Setup Solr, install Reddit schema

    $ sudo cp /usr/share/solr/example/webapps/solr.war /usr/share/solr/example/solr/
    $ sudo cp /usr/share/solr/example/lib/ext/* /usr/share/tomcat7/lib/
    $ sudo cp /usr/share/solr/example/resources/log4j.properties /usr/share/tomcat7/lib/
    $ sudo cp src/reddit/solr/schema4.xml /usr/share/solr/example/solr/collection1/conf/schema.xml
    $ sudo chown tomcat7:tomcat7 /usr/share/solr/example/solr/collection1/conf/schema.xml
 
Setup Tomcat for Solr

    $ sudo nano /usr/share/tomcat7/lib/log4j.properties
    # edit to set:
    solr.log=/usr/share/solr
 
    $ sudo nano /etc/tomcat7/Catalina/localhost/solr.xml
    # add content:
    <Context docBase="/usr/share/solr/example/solr/solr.war" debug="0" crossContext="true">
      <Environment name="solr/home" type="java.lang.String" value="/usr/share/solr/example/solr" override="true" />
    </Context>
 
    # have tomcat use port 8983 ('solr_port' in example.ini), port 8080 is haproxy
    sudo nano /etc/tomcat7/server.xml
    # edit to set:
    <Connector port="8983" protocol="HTTP/1.1"
 
    # Solr is missing some required stuff:
    $ sudo touch /usr/share/solr/solr.log
    $ sudo mkdir /usr/share/tomcat7/temp
    $ sudo chown tomcat7:tomcat7 /usr/share/solr/solr.log
    $ sudo chown tomcat7:tomcat7 /usr/share/tomcat7/temp
 
    # verify tomcat all good (ignore warnings):
    $ /usr/share/tomcat7/bin/configtest.sh

Start solr:

    $ sudo service tomcat7 restart
    # any errors logged must be fixed
    $ sudo cat /var/log/tomcat7/catalina.out
    # verify working, these should return html pages:
    $ wget 127.0.0.1:8983
    $ wget 127.0.0.1:8983/solr

Index site content and test:

    $ sudo start reddit-job-solr_subreddits
    $ sudo start reddit-job-solr_links
    # do a search on the site, verify working


---

## SaidIt Dev Guide

### Locally mounting VM or server files

    $ sudo apt-get install sshfs
    $ mkdir ~/vm
    $ sshfs reddit@reddit.local:/home/reddit/src/reddit ~/vm
    # optionally unmount it later with:
    $ fusermount -u ~/vm

### Logging

    $ sudo tail -f /var/log/syslog
    > g.log.warning("hello log")

### Profiling

Set `profile_directory` in `development.update` to an absolute path and create the directory first. cProfile results can be [viewed with pstats](https://web.archive.org/web/20180706112510/http://stefaanlippens.net/python_profiling_with_pstats_interactive_mode/).

### Memory by process

    ps aux  | awk '{print $6/1024 " MB\t\t" $11}'  | sort -n

### Installation profiles

#### app

    $ sudo INSTALL_PROFILE=app ./install/reddit.sh

installs the web and application tiers, including: nginx, haproxy, gunicorn, mcrouter, memcached (for stalecaches), and r2. no cron jobs or app services run.

app server(s) development.update configuration:

    main_db =      reddit,   remote-ip, *,    *,    *,    *,    *
    cassandra_seeds = remote-ip:9160
    lockcaches = remote-ip:11211
    permacache_memcaches = remote-ip:11211
    stalecaches = 127.0.0.1:11211
    hardcache_memcaches = remote-ip:11211
    amqp_host = remote-ip:5672
    activity_endpoint = remote-ip:9002
    geoip_location = http://remote-ip:5000
    solr_search_host = remote-ip
    solr_doc_host = remote-ip
    solr_subreddit_search_host = remote-ip
    solr_subreddit_doc_host = remote-ip
    # ensure these settings match the backend:
    # precompute_limit, precompute_limit_hot, hot_period_seconds, hot_max_links_per_subreddit 

app server(s) misc. configuration:

* `/etc/mcrouter/global.conf` set your remote memcached server ip(s) in `servers`
* `/etc/haproxy/haproxy.cfg` for `backend media` set `server nginx remote-ip:9000 maxconn 20`
* `/etc/haproxy/haproxy.cfg` for `backend pixel` set `server nginx remote-ip:8082 maxconn 20`

ensure backend server(s) development.update configuration:

    cassandra_seeds = remote-interface-ip:9160
    amqp_host = remote-interface-ip:5672
    activity_endpoint = remote-interface-ip:9002
    geoip_location = http://remote-interface-ip:5000

ensure backend server(s) misc. configuration:

* firewalls: open ports 5000/geoip, 5432/postgres, 5672/amqp/rabbitmq, 8082/pixel/click, 8983/solr, 9000/media, 9002/activity, 9160/cassandra, 11211/memcached as needed for trusted ips
* /etc/postgresql/9.3/main/postgresql.conf `listen_addresses = '*'` to listen on all interfaces
* /etc/cassandra/cassandra.yaml
  * `- seeds: "remote-interface-ip"`
  * `listen_address: remote-interface-ip`
  * `rpc_address: 0.0.0.0` to listen on all interfaces
* /etc/memcached.conf omit `-l` to listen on all interfaces
* /etc/init/reddit-activity.conf `--bind remote-interface-ip:9002`
* /etc/gunicorn.d/geoip.conf `--bind=remote-interface-ip:5000`

### Use a custom domain

Rather than accessing the site/app at https://reddit.local you can use your own domain. Change the configuration values for `domain` and `oauth_domain` in the main configuration file, `src/reddit/r2/development.update`. You should also update your SSL certificate accordingly, see the next section.

### Certbot/LetsEncrypt SSL Certificates

    $ sudo add-apt-repository ppa:certbot/certbot
    $ sudo apt-get update
    $ sudo apt-get install certbot
    $ sudo certbot certonly --manual --preferred-challenges dns -d you.net -d www.you.net -d m.you.net -d oauth.you.net
    $ sudo usermod -aG ssl-cert reddit
    $ sudo usermod -aG ssl-cert irc
    $ sudo chown -h reddit:ssl-cert /etc/letsencrypt/live/you.net/privkey.pem
    $ sudo chmod g+r /etc/letsencrypt/live/you.net/privkey.pem

Re-configure your services for your new cert:

    /etc/nginx/sites-available/reddit-ssl
    /etc/reddit/.lounge/config.js
    /unrealircd/conf/unrealircd.conf

Renew your cert every 90 days:

    $ sudo certbot renew

### SSL upgrade, for improved "Suggest Title" compatibility

#### Upgrade curl

Ubuntu 14 comes with curl 7.35.0. Upgrade it for improved SSL compatibility, particularly for "suggest title" and other remote fetching.

    $ sudo apt-get remove curl libcurl3
    $ sudo apt-get install build-essential
    # substitute version from https://curl.haxx.se/download.html
    $ wget https://curl.haxx.se/download/curl-7.65.1.tar.bz2
    $ tar -xvjf curl-7.65.1.tar.bz2
    $ cd curl-7.65.1
    $ ./configure --prefix=/usr
    $ make
    $ sudo make install
    $ sudo ldconfig
    $ curl --version
    $ cd ..
    $ rm -rf curl-7.65.1*

#### Upgrade python

Ubuntu 14 LTS provides python 2.7.6 but it's upgradable to at least 2.7.16 which modernizes SSL support.

WARNING: this currently breaks Cython dependencies in reddit PPAs/repos, so `install-reddit.sh` will fail with this upgrade in place. Don't upgrade until you have completed installation.

    $ sudo add-apt-repository ppa:jonathonf/python-2.7
    $ sudo apt-get update
    $ sudo apt-get install python2.7
    $ python --version

#### Rebuild reddit open source

    $ sudo apt-get install python-dev libxml2-dev libxslt1-dev zlib1g-dev
    $ cd ~/src/reddit/r2
    $ sudo reddit-stop
    $ python setup.py build
    $ sudo python setup.py develop
    $ make clean
    $ make build/mangle-buildstamp
    $ make -j $(nproc)
    $ sudo reddit-start
    $ sudo reddit-flush

---

## Next Steps

* [admin guide](https://github.com/libertysoft3/saidit/wiki/Admin-guide)
* [install chat](https://github.com/libertysoft3/saidit/wiki/Chat#saidit-chat-installation)

## Additional documentation

* https://github.com/libertysoft3/saidit/wiki
* https://web.archive.org/web/20191121131055/https://qconsf.com/sf2017/system/files/presentation-slides/qconsf-20171113-reddits-architecture.pdf
* [r/RedditOpenSource](https://www.reddit.com/r/RedditOpenSource)
* [r/redditdev](https://www.reddit.com/r/redditdev)

## See also

* [r/RedditAlternatives](https://www.reddit.com/r/RedditAlternatives)


