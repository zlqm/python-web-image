# python web image

## feature

* based on `phusion/baseimage` 
* use `runit` as process manager
* add `nginx` as reverse proxy and static file server 

```bash
~# pstree
my_init─┬─runsvdir─┬─runsv───cron
        │          ├─runsv
        │          ├─runsv───run───gunicorn───12*[gunicorn]
        │          └─runsv───nginx───12*[nginx]
        └─syslog-ng
```

## how to build

```
make
```

## how to use

### nginx

1. add global block config to `/etc/nginx/main.d/`
2. addd http block config to `/etc/nginx/conf.d/`
3. add server block config to `/etc/nginx/sites-enabled/`

### gunicorn

In default mode, you should put your app source code to `/app`, and expose wsgi app to /app/app:app.
You can change default settings by overwriting config file.

* default gunicorn config locates at `/etc/gunicorn.py`
* gunicorn start entry locates at `/etc/service/gunicorn/run`
