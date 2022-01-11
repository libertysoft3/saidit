FROM ubuntu:14.04

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install software-properties-common
RUN apt-add-repository -y ppa:reddit/ppa
COPY apt-preferences /etc/apt/preferences.d/reddit
RUN apt-get update

# reddit forked version mcrouter_0.10.0-0reddit1
RUN apt-get -y install mcrouter

# has docker compose service name "memcached" hardcoded
COPY global.conf /etc/mcrouter/global.conf

EXPOSE 5050

USER Debian-mcrouter

CMD mcrouter -f /etc/mcrouter/global.conf -L /var/log/mcrouter/mcrouter.log -p 5050 --num-proxies=1 -R /././ --stats-root=/var/mcrouter/stats

# verify working: https://shouts.dev/test-memcached-using-telnet-commands