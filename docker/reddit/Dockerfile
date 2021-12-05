FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get -y upgrade

# locale stuff
RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales
ENV LANG en_US.UTF-8

# reddit app
RUN apt-get -y install wget
RUN useradd --create-home --shell /bin/bash reddit
RUN usermod -aG sudo reddit
WORKDIR /home/reddit
# TODO: change 'docker' back to 'master'
ADD https://raw.github.com/libertysoft3/saidit/docker/install-reddit.sh install-reddit.sh
RUN chmod +x install-reddit.sh
RUN yes | REDDIT_DOMAIN=reddit.local REDDIT_USER=reddit REDDIT_HOME=/home/reddit INSTALL_PROFILE=docker ./install-reddit.sh

# cron
RUN apt-get -y install cron
RUN touch /var/log/cron.log
RUN apt-get -y install cron

EXPOSE 8001

# init scripts
COPY docker/reddit/init_cassandra.sh init_cassandra.sh
RUN chmod +x init_cassandra.sh
COPY docker/reddit/wrapper.sh wrapper.sh
RUN chmod +x wrapper.sh

CMD ["./wrapper.sh"]