#!/bin/bash
current_broker=$(ls /usr/local/Cellar/kafka/3.1.0/.bottle/etc/kafka | grep server | wc -l)

echo "previous brokers: ${current_broker}"

new_broker_cnt=`expr $current_broker + 1`

cp /usr/local/Cellar/kafka/3.1.0/.bottle/etc/kafka/server.properties /usr/local/Cellar/kafka/3.1.0/.bottle/etc/kafka/server_$new_broker_cnt.properties

new_broker=$(ls /usr/local/Cellar/kafka/3.1.0/.bottle/etc/kafka | grep server | wc -l)

echo "Successfully add 1 broker. Current broker:${new_broker}"  
