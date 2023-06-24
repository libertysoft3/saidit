### Archived

Recommended alternative repo: https://github.com/CrystalVulpine/saidit

## SaidIt

SaidIt is a [reddit open source](https://github.com/reddit-archive/reddit) continuation and fork with:

* critical bug fixes and documentation
* configurable site branding and home page
* enhanced expandos/embeds: more media providers, direct media links, expandos in comments/sidebars/wiki pages
* admin user bans and ip bans

Optional SaidIt features include:

* two dimensional voting and content sorting where insightful is +2 and fun is +1
* public moderator logs
* [web IRC](https://github.com/libertysoft3/lounge-autoconnect) chat integration

There are two supported installation methods- Docker or an Ubuntu 14 LTS server. Docker is recommended for production use and comes pre-configured for maximum performance. Running Ubuntu 14 LTS in a virtual machine is more flexible and is recommended for development use. Both approaches can be accomplished with Windows, MacOS, or Linux. Both approaches require that you make DNS changes to your machine to resolve https://reddit.local to your server.

## Docker installation

The instructions assume that you are using Ubuntu 20 LTS as your Docker host.

### Prepare host OS

    $ sudo apt update && sudo apt -y upgrade
    $ sudo apt install nginx docker docker-compose git
    $ sudo usermod -a -G docker $USER
    $ sudo systemctl enable docker && sudo systemctl restart docker
    # or logout and login again to reload your group permissions
    $ exec su -l $USER

Optionally fix any DNS timeout issues, for virtual machines (warning is Google DNS)

    $ sudo apt install resolvconf
    $ sudo sed -i "1i nameserver 8.8.4.4" /etc/resolv.conf && sudo sed -i "1i nameserver 8.8.8.8" /etc/resolv.conf
    $ sudo systemctl enable resolvconf.service && sudo systemctl restart resolvconf.service

### Install reddit open source

    $ cd ~
    $ git clone https://github.com/libertysoft3/saidit.git
    $ cp saidit/docker-compose.yml . && cp -r saidit/docker .
    $ rm -rf saidit
    $ docker-compose up -d

### Configure host OS's nginx

    $ sudo cp docker/host/nginx/reddit-ssl /etc/nginx/sites-available/reddit-ssl
    $ sudo ln -s /etc/nginx/sites-available/reddit-ssl /etc/nginx/sites-enabled/reddit-ssl
    $ sudo openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout /etc/ssl/private/key.pem -out /etc/ssl/certs/cert.pem
    $ sudo openssl dhparam -out /etc/ssl/dhparam.pem 2048
    $ sudo nginx -t
    $ sudo service nginx restart

## Ubuntu 14 installation

These instructions assume that you have setup a [VirtualBox](https://www.virtualbox.org/wiki/Downloads) virtual machine running [Ubuntu 14.04](http://releases.ubuntu.com/14.04/) with 2+ CPU cores, 4GB of RAM, 30GB of disk space, user 'reddit' and OpenSSH server. Connecting to your virtual machine using SSH is recommended for easy copy and paste.

### Install reddit open source

Run the installer

    $ wget --no-check-certificate https://raw.github.com/libertysoft3/saidit/master/install-reddit.sh
    $ chmod +x install-reddit.sh
    $ sudo ./install-reddit.sh

The installer should complete with success message "Congratulations! reddit is now installed". Do not proceed unless you see this message.

Option A: start with an empty reddit

    $ cd ~/src/reddit
    $ reddit-run scripts/inject_test_data.py -c 'inject_configuration_data()'
    $ sudo start reddit-job-update_reddits

Option B: populate sample user data including posts, comments, and subs

    $ cd ~/src/reddit
    $ reddit-run scripts/inject_test_data.py -c 'inject_test_data()'
    $ sudo start reddit-job-update_reddits

### Install search
 
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

    $ sudo sed -i "s/^solr.log=.*$/solr.log=\/usr\/share\/solr/" /usr/share/tomcat7/lib/log4j.properties
 
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

## Configure DNS for reddit.local

To access your reddit open source app, you must be able to resolve https://reddit.local to your Docker host or virtual machine. First, find the ip address of your Docker host or virtual machine. Then update your 'hosts' file (on your desktop or wherever your web browser is running). On linux, update `/etc/hosts`, on Windows and MacOS, see https://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/

## Next steps

* access reddit open source at https://reddit.local
* login and change the passwords of accounts 'reddit' and 'automoderator', they have default password 'password'
* [admin guide](https://github.com/libertysoft3/saidit/wiki/Admin-guide)
* [dev guide](https://github.com/libertysoft3/saidit/wiki/Dev-guide)
* [install chat](https://github.com/libertysoft3/saidit/wiki/Chat#saidit-chat-installation)

## See also

* [r/RedditOpenSource](https://www.reddit.com/r/RedditOpenSource)
* [r/redditdev](https://www.reddit.com/r/redditdev)
* [r/RedditAlternatives](https://www.reddit.com/r/RedditAlternatives)

![Image of Saidit logo](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTWA5A1rZZJu_oFjSkUk42Ds5-UDm6c9HNkwSngMYAtvc_Dybkt)
