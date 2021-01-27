import logging
import os
import multiprocessing
import gevent.monkey
import psycopg2
from gevent.socket import wait_read, wait_write

bind = 'unix:/tmp/gunicorn.sock'
chdir = '/app'
timeout = 30
worker_class = 'gevent'

workers = multiprocessing.cpu_count()
loglevel = 'info'
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
accesslog = "/var/log/gunicorn_access.log"
errorlog = "/var/log/gunicorn_error.log"


def gevent_wait_callback(conn, timeout=None):
    """A wait callback useful to allow gevent to work with Psycopg."""
    # Copyright (C) 2010-2012 Daniele Varrazzo <daniele.varrazzo@gmail.com>
    # This function is borrowed from psycogreen module which is licensed
    # under the BSD license (see in odoo/debian/copyright)
    while 1:
        state = conn.poll()
        if state == psycopg2.extensions.POLL_OK:
            break
        elif state == psycopg2.extensions.POLL_READ:
            wait_read(conn.fileno(), timeout=timeout)
        elif state == psycopg2.extensions.POLL_WRITE:
            wait_write(conn.fileno(), timeout=timeout)
        else:
            raise psycopg2.OperationalError("Bad result from poll: %r" % state)


gevent.monkey.patch_all()
psycopg2.extensions.set_wait_callback(gevent_wait_callback)
