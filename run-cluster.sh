#!/bin/bash

echo "Launch MySQL, RabbitMQ, Memcached, ElasticSearch nodes:"
docker-compose -f docker-compose-kafka.yml up -d db broker memcached es
echo "Launch 3x Zookeeper and 3x Kafka instances"
docker-compose -f docker-compose-kafka.yml up -d zoo1 zoo2 zoo3 kafka1 kafka2 kafka3
echo "Wait until services are up and running..."
sleep 10
echo "Run database migrations"
docker-compose -f docker-compose-kafka.yml run web python manage.py migrate
echo "Launch Celery task runner and flower(monitoring)"
docker-compose -f docker-compose-kafka.yml up -d celery flower
echo "Done!"
