FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONBUFFERED 1
# for reddit installer on container build
ENV REDDIT_HOME /home/reddit
ENV REDDIT_DOMAIN reddit.local
ENV INSTALL_PROFILE docker
ENV REDDIT_PLUGINS ''
# for container init
ENV CASSANDRA_HOST cassandra
ENV CASSANDRA_PORT 9160
ENV POSTGRES_HOST postgres
ENV POSTGRES_PORT 5432
# for reddit app, replaces sourcing /etc/default/reddit
ENV REDDIT_ROOT /home/reddit/src/reddit/r2
ENV REDDIT_INI /home/reddit/src/reddit/r2/run.ini
ENV REDDIT_USER reddit
ENV REDDIT_GROUP nogroup
ENV REDDIT_CONSUMER_CONFIG /home/reddit/consumer-count.d
ENV REDDIT_SRC /home/reddit/src

RUN apt-get update
RUN apt-get -y upgrade

# locale stuff
RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales
ENV LANG en_US.UTF-8

# supervisor, cron
RUN apt-get -y install cron supervisor
RUN mkdir -p /var/log/supervisor
COPY docker/reddit/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN touch /var/log/cron.log
RUN apt-get -y install cron

# reddit app
RUN apt-get -y install sudo wget
RUN useradd --create-home --shell /bin/bash reddit
RUN echo "reddit:password" | chpasswd
RUN adduser reddit sudo

WORKDIR /home/reddit
# TODO: change 'docker' back to 'master'
ADD https://raw.github.com/libertysoft3/saidit/docker/install-reddit.sh install-reddit.sh
RUN chmod +x install-reddit.sh
RUN yes | ./install-reddit.sh

EXPOSE 8001

# supervisor cannot easily the control order of execution, so
# initialize the container with a shell script
COPY docker/reddit/init_container.sh init_container.sh
RUN chmod +x init_container.sh
COPY docker/reddit/init_cassandra.sh /home/reddit/init_cassandra.sh
RUN chmod +x /home/reddit/init_cassandra.sh

CMD ["./init_container.sh"]