docker run \
	--name=kafka-ui \
	--hostname=129c104c5dc9 \
	--user=kafkaui \
	--env=KAFKA_CLUSTERS_0_NAME=local \
	--env=KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=localhost:9092 \
	--env=KAFKA_CLUSTERS_0_KAFKACONNECT_0_NAME=local \
	--env=KAFKA_CLUSTERS_0_KAFKACONNECT_0_ADDRESS=http://kafka-connect:8083 \
	--env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
	--env=JAVA_OPTS= \
	--network=kafka_default \
	-p 8080:8080 \
	--restart=always \
	--label='com.docker.compose.service=kafka-ui' \
	--label='com.docker.compose.project.config_files=docker-compose.yaml' \
	--label='com.docker.compose.container-number=1' \
	--label='com.docker.compose.config-hash=80dc9885ce9d08b52f9ada000de91ea51d2766c73e3afb45796b976d111af155' \
	--label='com.docker.compose.version=1.29.2' \
	--label='com.docker.compose.project=kafka' \
	--label='com.docker.compose.project.working_dir=/Users/linyanliang/experiment/data_streaming/kafka' \
	--label='com.docker.compose.oneoff=False' \
	--runtime=runc \
	--detach=true \
	provectuslabs/kafka-ui:master \
	/bin/sh -c 'java $JAVA_OPTS -jar kafka-ui-api.jar'
