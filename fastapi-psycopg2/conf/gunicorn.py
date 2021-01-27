import logging
import os
import multiprocessing

bind = 'unix:/tmp/gunicorn.sock'
chdir = '/app'
timeout = 30
worker_class = 'uvicorn.workers.UvicornWorker'

workers = multiprocessing.cpu_count()
loglevel = 'info'
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
accesslog = "/var/log/gunicorn_access.log"
errorlog = "/var/log/gunicorn_error.log"
