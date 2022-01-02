FROM rabbitmq:3.5.7

# for running things like:
# ./rabbitmqadmin -H rabbitmq -P 15672 -V / -u reddit -p reddit list queues
# ./rabbitmqadmin -H rabbitmq -P 15672 -V / -u reddit -p reddit purge queue name=event_collector
RUN rabbitmq-plugins enable --offline rabbitmq_management