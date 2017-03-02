#!/bin/bash

docker-compose -f docker-compose-kafka.yml up -d db broker memcached es
sleep 10
docker-compose -f docker-compose-kafka.yml run web python manage.py migrate
docker-compose -f docker-compose-kafka.yml up -d celery flower
sleep 5
docker-compose -f docker-compose-kafka.yml up web
