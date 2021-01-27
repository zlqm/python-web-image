FROM phusion/baseimage:bionic-1.0.0

RUN apt-get update && \
    apt-get upgrade -y && \
    apt install -y curl gnupg2 ca-certificates lsb-release &&\
    echo "deb http://nginx.org/packages/ubuntu `lsb_release -cs` nginx" | tee /etc/apt/sources.list.d/nginx.list && \
    curl -fsSL https://nginx.org/keys/nginx_signing.key | apt-key add - && \
    apt-key fingerprint ABF5BD827BD9BF62 && \
    apt update && \
    apt-get install nginx -y && \
    rm -rf /etc/nginx/conf.d/ /etc/nginx/sites-enabled/ && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY conf/nginx/nginx.conf /etc/nginx/nginx.conf
COPY conf/nginx/conf.d /etc/nginx/conf.d/
COPY conf/nginx/sites-enabled/ /etc/nginx/sites-enabled/
COPY conf/runit/nginx.sh /etc/service/nginx/run

COPY scripts/build_python.sh /bd_build/python.sh
RUN /bd_build/python.sh

# Clean up APT when done.
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.cache/pip
