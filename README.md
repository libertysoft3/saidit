SaidIt is a [reddit open source](https://github.com/reddit-archive/reddit) continuation and fork with:

* critical configurations restored
* critical bug fixes
* admin user bans and ip bans
* configurable site branding
* configurable home page
* enhanced expandos/embeds: more media providers, direct media links, expandos in comments/sidebars/wiki pages

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

# Installation

There are two ways to set up a saidit server: on a standalone physical server, or through a Virtual Machine environment (running within another OS such as linux, MacOS, or Windows) for development and testing purposes.

## Setting up a virtual machine

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

## Setting up a physical server

1. Download the latest [Ubuntu 14.04](http://releases.ubuntu.com/14.04/) server .ISO file "64-bit PC (AMD64) server install image"
1. Download [Rufus](https://rufus.ie/) (as recommended by Ubuntu) and use it to write the .ISO to a USB drive
1. Once finished, put the USB drive in the server and boot to it
1. Install Ubuntu with the following options, but leaving all other options with the default selection:
   1. Username: reddit
   1. Choose software to install: select OpenSSH, but no others
1. When install finishes, remove USB drive and boot to linux

From this point forward physical access to the server is no longer needed and you can ssh in as the 'reddit' user remotely if you wish, using a program like [PuTTY](https://www.putty.org/).


## Configure DNS for reddit.local

To use your reddit server, you are expected to be able to resolve reddit.local and https://reddit.local. First, find the ip address of your saidit server by running:

    $ ifconfig
    # note the 'inet addr' for device 'eth0' or similar

Then update your `hosts` file on your development machine/host OS. For example, on linux with saidit server ip 192.168.1.20  run:

    $ sudo sed -i '1i 192.168.1.20 reddit.local' /etc/hosts

For Windows and MacOS see https://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/


## Install reddit open source

SSH into your saidit server

    $ ssh reddit@reddit.local

Run the installer

    $ wget --no-check-certificate https://raw.github.com/libertysoft3/saidit/master/install-reddit.sh
    $ chmod +x install-reddit.sh
    $ sudo ./install-reddit.sh

The installer should complete with success message "Congratulations! reddit is now installed". Do not proceed unless you see this message.

Option A: start with an empty reddit

    $ cd ~/src/reddit
    $ reddit-run scripts/inject_test_data.py -c 'inject_configuration_data()'
    $ sudo start reddit-job-update_reddits

Option B: populate sample users, posts, comments, and subs

    $ cd ~/src/reddit
    $ reddit-run scripts/inject_test_data.py -c 'inject_test_data()'
    $ sudo start reddit-job-update_reddits


## Install search (optional)
 
Install Solr

    $ cd ~
    $ sudo apt-get install tomcat7 tomcat7-admin software-properties-common
    $ wget http://archive.apache.org/dist/lucene/solr/4.10.4/solr-4.10.4.tgz
    $ tar -xvzf solr-4.10.4.tgz
    $ sudo mv solr-4.10.4 /usr/share/solr
    $ sudo chown -R tomcat7:tomcat7 /usr/share/solr/example
 
Setup Solr and schema

    $ sudo cp /usr/share/solr/example/webapps/solr.war /usr/share/solr/example/solr/
    $ sudo cp /usr/share/solr/example/lib/ext/* /usr/share/tomcat7/lib/
    $ sudo cp /usr/share/solr/example/resources/log4j.properties /usr/share/tomcat7/lib/
    $ sudo cp ~/src/reddit/solr/schema4.xml /usr/share/solr/example/solr/collection1/conf/schema.xml
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

Start solr

    $ sudo service tomcat7 restart
    # any errors logged must be fixed
    $ sudo cat /var/log/tomcat7/catalina.out
    # verify working, these should return html pages:
    $ wget 127.0.0.1:8983
    $ wget 127.0.0.1:8983/solr

Index site content

    $ sudo start reddit-job-solr_subreddits
    $ sudo start reddit-job-solr_links

# Next steps

* access your site at https://reddit.local
* change the default password of 'password' for accounts 'reddit' and 'automoderator'
* [admin guide](https://github.com/libertysoft3/saidit/wiki/Admin-guide)
* [dev guide](https://github.com/libertysoft3/saidit/wiki/Dev-guide)
* [install chat](https://github.com/libertysoft3/saidit/wiki/Chat#saidit-chat-installation)

# See also

* [r/RedditOpenSource](https://www.reddit.com/r/RedditOpenSource)
* [r/redditdev](https://www.reddit.com/r/redditdev)
* [r/RedditAlternatives](https://www.reddit.com/r/RedditAlternatives)


