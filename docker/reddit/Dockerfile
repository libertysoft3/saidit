FROM ubuntu:14.04
LABEL Author="libertysoft3"

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install wget

RUN useradd --create-home --shell /bin/bash reddit
# RUN usermod -aG sudo reddit
WORKDIR /home/reddit

# USER root
RUN wget https://raw.github.com/libertysoft3/saidit/master/install-reddit.sh

RUN chmod +x install-reddit.sh
RUN yes | REDDIT_DOMAIN=reddit.local REDDIT_USER=reddit REDDIT_HOME=/home/reddit INSTALL_PROFILE=docker ./install-reddit.sh

# Add all files from current directory on host to dockerised-example directory in container 
# ADD ./ /dockerised-example/
# COPY docker/entrypoint.sh /sbin/entrypoint.sh

# Expose a port so that we can map it with a host port
EXPOSE 8001

# USER reddit

# Execute command when container starts (not executed with image build)
# ENTRYPOINT ["/sbin/entrypoint.sh"]
