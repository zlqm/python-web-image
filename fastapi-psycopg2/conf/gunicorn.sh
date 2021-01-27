#!/bin/bash

set -e

gunicorn -c /etc/gunicorn.py app:app
