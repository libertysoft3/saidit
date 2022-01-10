# chose ubuntu 14 for convenience, newer OSes and existing docker images can also run solr 4
FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONBUFFERED 1

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install software-properties-common wget tomcat7 tomcat7-common tomcat7-admin libtomcat7-java

RUN wget http://archive.apache.org/dist/lucene/solr/4.10.4/solr-4.10.4.tgz
RUN tar -xvzf solr-4.10.4.tgz
RUN mkdir -p /usr/share/solr
RUN cp -r solr-4.10.4/* /usr/share/solr/
RUN cp /usr/share/solr/example/webapps/solr.war /usr/share/solr/example/solr/
RUN cp /usr/share/solr/example/lib/ext/* /usr/share/tomcat7/lib/
RUN cp /usr/share/solr/example/resources/log4j.properties /usr/share/tomcat7/lib/
ADD https://raw.github.com/libertysoft3/saidit/master/solr/schema4.xml /usr/share/solr/example/solr/collection1/conf/schema.xml
RUN chown -R tomcat7:tomcat7 /usr/share/solr/example
RUN touch /usr/share/solr/solr.log && chown tomcat7:tomcat7 /usr/share/solr/solr.log
RUN mkdir -p /usr/share/tomcat7/temp && chown tomcat7:tomcat7 /usr/share/tomcat7/temp
RUN mkdir -p /usr/share/tomcat7/logs && chown tomcat7:tomcat7 /usr/share/tomcat7/logs
RUN sed -i "s/^solr.log=.*$/solr.log=\/usr\/share\/solr/" /usr/share/tomcat7/lib/log4j.properties
COPY solr.xml /etc/tomcat7/Catalina/localhost/solr.xml
RUN sed -i "s/<Connector port=.*$/<Connector port='8983' protocol='HTTP\/1.1'/" /etc/tomcat7/server.xml

# https://bugs.launchpad.net/ubuntu/+source/tomcat7/+bug/1232258
RUN ln -s /var/lib/tomcat7/common/  /usr/share/tomcat7/common
RUN ln -s /var/lib/tomcat7/server/  /usr/share/tomcat7/server
RUN ln -s /var/lib/tomcat7/shared/  /usr/share/tomcat7/shared
RUN ln -s /var/lib/tomcat7/conf/    /usr/share/tomcat7/conf

CMD ["/usr/share/tomcat7/bin/catalina.sh", "run"]

# verify configuration valid
# $ /usr/share/tomcat7/bin/catalina.sh configtest
# logs
# $ tail -f /usr/share/tomcat7/logs/*
