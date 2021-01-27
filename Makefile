.PHONY: help, python-web, gevent-psycopg2, fastapi-psycopg2

help:
	echo "make {build-python-web|build-gevent-psycopg2}"

python-web:
	docker build python-web -t python-web

gevent-psycopg2:
	docker build gevent-psycopg2 -t gevent-psycopg2

fastapi-psycopg2:
	docker build fastapi-psycopg2 -t fastapi-psycopg2
