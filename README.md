# SaidIt

[SaidIt](https://saidit.net) is a [reddit open source](https://github.com/reddit-archive/reddit) continuation and fork. Major SaidIt changes include:

* configurable site branding
* critical features, cron jobs, and configurations restored
* admin tools including global user bans and ip bans
* more embedable media services
* configurable home page

User-facing SaidIt changes include:

* two dimensional voting where insightful is +2 and fun is +1
* markdown media expandos
* public moderator logs
* chat integration with a custom [TheLounge](https://github.com/libertysoft3/lounge-autoconnect) web IRC client

Goals:

* reddit API compatibility
* platform upgrades, longevity
* easily setup your own reddit or saidit clone

---

## Installation

There are two ways to set up a saidit server: on a standalone physical server, or through a Virtual Machine environment (running within another OS such as linux, MacOS, or Windows) for development and testing purposes.

### Setting up a virtual machine

1. Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
1. Download [Ubuntu 14.04.6](http://releases.ubuntu.com/14.04/) server install image
1. Start VirtualBox and click 'New'
   1. Type: Linux
   1. Version: Ubuntu (64-bit)
   1. Memory Size: 4000 MB (minimum)
   1. File location and size: 30.0 GB (minimim)
1. Right click the new VM and choose 'Settings'
   1. Network: Adapter 1: Attached to: "Bridged Adapter"
   1. Storage: Click "Choose Virtual Optical Disk File" and select the Ubuntu 14 .iso you file previously downloaded
1. Select the new VM and click 'Start'
1. Install Ubuntu with the following options, but leaving all other options with the default selection:
   1. username "reddit"
   1. "Choose software to install": Select OpenSSH, but no others
1. Complete Ubuntu installation

From this point forward you can start your VM with 'Start -> Headless Start' and ssh in as the 'reddit' user if you wish, using a program like [PuTTY](https://www.putty.org/). Don't forget to shut down your VM with 'Close -> ACPI Shutdown' before shutting down your host OS or you may corrupt your VM.

### Setting up a physical server

1. Download the [Ubuntu 14.04.6](http://releases.ubuntu.com/14.04/) Server Amd64 (64-bit version) .ISO file
1. Download [Rufus](https://rufus.ie/) (as recommended by Ubuntu) and use it to write the .ISO to a USB drive
1. Once finished, put the USB drive in the server and boot to it
1. Install Ubuntu with the following options, but leaving all other options with the default selection:
   1. username: reddit
   1. "Choose software to install": Select OpenSSH, but no others
1. When install finishes, remove USB drive and boot to linux

From this point forward physical access to the server is no longer needed and you can ssh in as the 'reddit' user remotely if you wish, using a program like [PuTTY](https://www.putty.org/).


### Connecting to your saidit/reddit open source server

This step is optional and for convenience but is highly recommended. These instructions will help you update your hosts file to resolve https://reddit.local (to your saidit server) in both your browser and your SSH client.

#### Find the ip address of your saidit server

    $ ifconfig
    # note the 'inet addr' for device 'eth0'

#### Update the 'hosts' file on your development machine/host OS

E.g. host OS linux and saidit server ip 192.168.1.20:

    $ sudo sed -i '1i 192.168.1.20 reddit.local' /etc/hosts

Instructions for Windows and MacOS: https://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/


### Install saidit

SSH into your saidit server and update the OS

    $ ssh reddit@reddit.local
    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo apt-get install git gperf

Install saidit

    $ cd ~/
    $ git clone https://github.com/libertysoft3/saidit.git
    $ chmod +x saidit/install-reddit.sh
    $ sudo ./saidit/install-reddit.sh
    # do not proceed if the installer printed any errors
    # cleanup installation, saidit has been installed elsewhere:
    $ rm -rf ~/saidit
 
### Upgrade curl

This will improve the new link 'fetch title' capability and potentially more

    $ sudo apt-get build-dep curl
    # use latest stable curl version from https://curl.haxx.se
    $ wget https://curl.haxx.se/download/curl-7.64.1.tar.bz2
    $ tar -xvjf curl-7.64.1.tar.bz2
    $ cd curl-7.64.1
    $ ./configure --prefix=/usr
    $ make
    $ sudo make install
    $ sudo ldconfig
    $ curl --version
 
 
### Upgrade to python 2.7

TODO: if you upgrade python before running install-reddit.sh, install-reddit.sh will error out on cython dependencies
TODO: is this upgrade necessary on Ubuntu 14?
 
    $ sudo add-apt-repository ppa:jonathonf/python-2.7
    $ sudo apt-get update
    $ sudo apt-get install python2.7
    $ python --version

### Upgrade gcc

    $ sudo add-apt-repository ppa:ubuntu-toolchain-r/test
    $ sudo apt-get update
    $ sudo apt-get install gcc-4.9 g++-4.9 cpp-4.9
    $ cd /usr/bin
    $ sudo rm gcc g++ cpp x86_64-linux-gnu-gcc
    $ sudo ln -s gcc-4.9 gcc
    $ sudo ln -s g++-4.9 g++
    $ sudo ln -s cpp-4.9 cpp
    $ sudo ln -s x86_64-linux-gnu-gcc-4.9 x86_64-linux-gnu-gcc

### Rebuild reddit
 
    $ sudo reddit-stop
    $ sudo reddit-flush
    $ sudo apt-get install libxml2-dev libxslt1-dev python-dev
    $ cd ~/src/reddit/r2
    $ python setup.py build
    $ sudo python setup.py develop
    $ make clean
    $ make
    $ sudo reddit-start

### Install sample data

This also creates a reddit admin user "saidit" with password "password".

    $ cd ~/src/reddit
    $ reddit-run scripts/inject_test_data.py -c 'inject_test_data()'
    $ sudo reddit-restart

---

## Install Solr for search
 
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
 
    # have tomcat use port 8983 (see 'solr_port' in example.ini)
    # port 8080 is taken by haproxy
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
    # any errors in here must be fixed
    $ sudo cat /var/log/tomcat7/catalina.out
    # verify working, these should return html pages:
    $ wget 127.0.0.1:8983
    $ wget 127.0.0.1:8983/solr

 
### Add reddit content to Solr:

    $ cd ~/src/reddit/r2
    $ paster run run.ini -c 'import r2.lib.providers.search.solr as cs; cs.rebuild_subreddit_index()'
    $ paster run run.ini -c 'import r2.lib.providers.search.solr as cs; cs._rebuild_link_index()'
    # do a search on the site, verify working
 
 
### Setup Solr cron jobs:
 
    $ sudo nano /etc/init/reddit-job-solr_subreddits.conf
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

 
    $ sudo nano /etc/init/reddit-job-solr_links.conf
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
 
 TODO: assume Solr will be installed, add these two jobs to the codebase/installer.

---

## Install SaidIt Chat

In a production environments, irc and related services should be run by a dedicated unix user for security.

### Install unreal irc server

    $ sudo apt-get install make gcc build-essential openssl libssl-dev libcurl4-openssl-dev zlib1g zlib1g-dev zlibc libgcrypt11 libgcrypt11-dev
    # UPDATE to the latest stable release
    $ wget https://www.unrealircd.org/unrealircd4/unrealircd-4.2.0.tar.gz
    $ tar xzvf unrealircd-4.2.0.tar.gz
    $ cd unrealircd-4.2.0/
    $ ./Config
    # space to read the license, press [Enter] a bunch of times to install, for "Do you want to generate an SSL certificate for the IRCd?" respond "No"
    $ make
    $ make install

use the reddit.local SSL cert with unreal:

    $ sudo cp /etc/ssl/certs/ssl-cert-snakeoil.pem ~/unrealircd/conf/ssl/server.cert.pem
    $ sudo cp /etc/ssl/private/ssl-cert-snakeoil.key ~/unrealircd/conf/ssl/server.key.pem
    # assuming you are installing as user 'reddit':
    $ sudo chown reddit:reddit ~/unrealircd/conf/ssl/*

configure unreal:

    $ cd ~/unrealircd
    $ cp conf/examples/example.conf conf/unrealircd.conf
    # edit conf/unrealircd.conf and change:
    #   change 'oper bobsmith' to `oper ircoperator`
    #   change 'password "test";' to a unique password
    #   section 'cloak-keys' needs 2 keys added
    #   set 'kline-address' to an email address
    #   set 'maxchannelsperuser' t0 50
    #   in 'allow' block for ip '*@*' change 'maxperip' to 10
    #   add a new allow block: allow { ip *@127.0.0.1; class clients; maxperip 50000; };

configure unreal for anope services. add the following to `~/unrealircd/conf/unrealircd.conf`, before `ulines`:

    link services.reddit.local
    {
        incoming {
                mask *@127.0.0.1;
        };
        outgoing {
                bind-ip *; /* or explicitly an IP */
                hostname services.reddit.local;
                port 6900;
                options { ssl; };
        };
        password "my-services-password-1234";
        class servers;
    };

change `ulines` to:

    ulines {
      services.reddit.local;
    };

start unreal:

    $ ./unrealircd start

cleanup, substitute your version number where appropriate:

    $ cd ~
    $ rm -rf unrealircd-4.2.0
    $ rm unrealircd-4.2.0.tar.gz

### Install anope IRC services

This provides ListServ, ChanServ, etc.

    $ cd ~
    $ sudo apt-get install cmake build-essential
    # update version number to the latest stable release:
    $ wget https://github.com/anope/anope/releases/download/2.0.6/anope-2.0.6-source.tar.gz
    $ tar xzvf anope-2.0.6-source.tar.gz
    $ cd anope-2.0.6-source
    $ ./Config
    # press [Enter] a bunch, accept defaults
    $ cd build/
    $ make
    $ make install

Configure anope:

    $ cd ~/services/conf/
    $ cp nickserv.example.conf nickserv.conf
    # edit nickserv.conf, set guestnickprefix = "guest" (for The Lounge autconnect feature)
    $ cp operserv.example.conf operserv.conf
    # NOTE: insecure if you allow outside access to IRC/6667, instead just change maxsessionlimit only and later run:
    #    /msg OperServ exception add +0 127.0.0.1 50000 Allow many localhost TheLounge clients
    # edit operserv.conf, set defaultsessionlimit = 50000, maxsessionlimit = 50000 (since everyone connects from localhost)
    $ cp example.conf services.conf
    # edit services.conf and set:
    # set uplink::ssl to 'yes'
    # set uplink::port to 6667
    # set uplink::password to 'my-services-password-1234'
    # set serverinfo::name to services.reddit.local
    # comment out the botserv include, search for `botserv.example.conf`
    # change `nickserv.example.conf` to `nickserv.conf`
    # change `operserv.example.conf` to `operserv.conf`
    # change `inspircd20` (in `module`) to `unreal4`

add this oper section near the existing disabled ones:

    oper
    {
        name = "ircoperator"
        type = "Services Root"
        require_oper = yes
    }

start anope:

    $ cd ~/services/bin
    $ ./services

cleanup, substitute your version number where appropriate:

    $ cd ~
    $ rm -rf anope-2.0.6-source
    $ rm anope-2.0.6-source.tar.gz

### Install TheLounge web IRC client

    $ cd ~
    $ git clone https://github.com/libertysoft3/lounge-autoconnect.git
    $ cd lounge-autoconnect
    # update to the latest autoconnect branch
    $ git checkout v2.4.0-autoconnect
    $ npm install
    $ NODE_ENV=production npm run build
    $ node index config
    # [ESC] : q to quit

configure TheLounge, SSL cert paths may need to be adjusted:

    $ nano ~/.lounge/config.js
    # edit to match:
    #   public: false,
    #   port: 2053,
    #   theme: "themes/zenburn.css",
    #   prefetch: true,
    #   prefetchStorage: true,
    #   prefetchMaxImageSize: 2048,
    #   lockNetwork: true,
    #   defaults { name: "saiditDEV", host: "127.0.0.1", nick: "guest", username: "guest", realname: "Guest", join: "#home" }
    #   https: { enable: true, key: "/home/reddit/unrealircd/conf/ssl/server.key.pem", certificate: "/etc/ssl/certs/ssl-cert-snakeoil.pem" }

add an intial user so the server will start:

    $ cd ~/lounge-autoconnect
    $ node index add firstuser
    # use a throwaway password, don't log to disk

start TheLounge:

    $ cd ~/lounge-autoconnect
    $ nohup npm start ./ > thelounge.log 2>&1 &

---

## SaidIt dev guide

You can mount the VM's reddit files as a folder on your host machine for easy editing and searching. On your host/development machine:

    $ sudo apt-get install sshfs
    $ mkdir ~/vm
    $ sshfs reddit@reddit.local:/home/reddit/src/reddit ~/vm
    # optionally unmount with:
    $ fusermount -u ~/vm

SaidIt log file, debug errors:

    $ sudo tail -f /var/log/syslog

Change the default subs:

    $ cd ~/src/reddit/r2
    $ paster shell run.ini
    # paste the following, hit enter:
    from r2.models import *
    srs = [Subreddit._by_name(n) for n in ("pics", "videos", "science", "technology")]
    LocalizedDefaultSubreddits.set_global_srs(srs)
    LocalizedFeaturedSubreddits.set_global_srs([Subreddit._by_name('pics')])
    exit()

Taking it to production:

    # change db_pass in example.ini and /etc/cron.d/reddit
    # change saidit user saidit's password
    # install fail2ban
    # configure your firewall
    debug = false
    uncompressedJS = false

---

## Additional documentation

* [https://www.reddit.com/r/RedditOpenSource](https://www.reddit.com/r/RedditOpenSource)
* [https://github.com/reddit-archive/reddit/wiki](https://github.com/reddit-archive/reddit/wiki)
* [https://www.reddit.com/r/redditdev](https://www.reddit.com/r/redditdev)

---

## See also

* https://www.reddit.com/r/RedditAlternatives


