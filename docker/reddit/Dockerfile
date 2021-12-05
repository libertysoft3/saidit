FROM ubuntu:14.04
LABEL Author="libertysoft3"

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install wget

RUN useradd --create-home --shell /bin/bash reddit
# RUN usermod -aG sudo reddit
WORKDIR /home/reddit

# TODO - change 'docker' back to 'master'
RUN wget https://raw.github.com/libertysoft3/saidit/docker/install-reddit.sh
RUN chmod +x install-reddit.sh
RUN yes | REDDIT_DOMAIN=reddit.local REDDIT_USER=reddit REDDIT_HOME=/home/reddit INSTALL_PROFILE=docker ./install-reddit.sh

# startup/init script
COPY docker/reddit/init-cassandra.sh /docker-entrypoint-initdb.d/init-cassandra.sh

# Expose a port so that we can map it with a host port
EXPOSE 8001

# USER reddit

# Execute command when container starts (not executed with image build)
# ENTRYPOINT ["/sbin/entrypoint.sh"]
