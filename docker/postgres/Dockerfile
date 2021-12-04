FROM postgres:9.3.24
LABEL Author="libertysoft3"

RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

COPY docker/postgres/init-reddit-db.sh /docker-entrypoint-initdb.d/init-reddit-db.sh