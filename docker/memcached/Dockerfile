FROM ubuntu:14.04
LABEL Author="libertysoft3"

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install software-properties-common
RUN apt-add-repository -y ppa:reddit/ppa
COPY docker/apt-preferences /etc/apt/preferences.d/reddit
RUN apt-get update

# travis gives us a stock libmemcached.  We have to remove that
RUN apt-get remove -y $(dpkg-query  -W -f='${binary:Package}\n' | grep libmemcached | tr '\n' ' ')
RUN apt-get autoremove -y

# reddit forked version memcached_1.4.30-1reddit1~trusty1
RUN apt-get -y install memcached

# Expose a port so that we can map it with a host port
EXPOSE 11211

# SAIDIT: 64mb is the system default. Should be 1024mb+ in production.
# Also consider increasing -R and -I, especially if you increase precompute_limit.
CMD ["-m", "256"]

# Set the user to run Memcached daemon
USER daemon

# Set the entrypoint to memcached binary
ENTRYPOINT memcached

# verify working: https://shouts.dev/test-memcached-using-telnet-commands