FROM zlqm/python-web:latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3.8-dev libpq-dev libpq5 && \
    pip3 install psycopg2==2.8.6 gevent==21.1.2 gunicorn==20.0.4 && \
    apt-get remove -y gcc libpq-dev python3.8-dev && apt-get -y autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.cache/pip
