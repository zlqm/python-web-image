.PHONY: help, build-python-web, build-gevent-psycopg2

help:
	echo "make {build-python-web|build-gevent-psycopg2}"

build-python-web:
	docker build python-web -t python-web

build-gevent-psycopg2:
	docker build gevent-psycopg2 -t gevent-psycopg2
