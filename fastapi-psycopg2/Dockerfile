FROM zlqm/python-web:latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3.8-dev libpq-dev libpq5 && \
    pip3 install fastapi==0.63.0 gunicorn==20.0.4 pydantic==1.7.3 uvicorn[standard]==0.13.3 &&
    apt-get remove -y gcc libpq-dev python3.8-dev && apt-get -y autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.cache/pip
ADD conf/default.conf /etc/nginx/sites-enabled/default.conf
ADD conf/gunicorn.sh /etc/service/gunicorn/run
ADD conf/gunicorn.py /etc/gunicorn.py
ADD app.py /app/app.py

