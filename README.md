# Django Celery Example

- [Django Celery Example](#django-celery-example)
  - [Introduction](#introduction)
  - [systemd](#systemd)
    - [EnvironmentFile](#environmentfile)
    - [Celery Beat Service](#celery-beat-service)
    - [Celery Worker Service](#celery-worker-service)

## Introduction

A example shows how to use celery beat in django.

## systemd

### EnvironmentFile

- `/etc/conf.d/celery`

```ini
# Name of nodes to start
# here we have a single node
CELERYD_NODES="w1"
# or we could have three nodes:
# CELERYD_NODES="w1 w2 w3"

# Absolute or relative path to the 'celery' command:
CELERY_BIN="/data/app/venv/bin/celery"
# CELERY_BIN="/virtualenvs/def/bin/celery"

CELERYD_CHDIR="/data/app/proj"

CELERYBEAT_CHDIR="/data/app/proj"

# App instance to use
# comment out this line if you don't use an app
CELERY_APP="proj"
# or fully qualified:
# CELERY_APP="proj.tasks:app"

# How to call manage.py
CELERYD_MULTI="multi"

# Extra command-line arguments to the worker
CELERYD_OPTS="--time-limit=300 --concurrency=8"

# - %n will be replaced with the first part of the nodename.
# - %I will be replaced with the current child process index
#   and is important when using the prefork pool to avoid race conditions.
CELERYD_PID_FILE="/var/run/celery/%n.pid"
CELERYD_LOG_FILE="/var/log/celery/%n.log"
CELERYD_LOG_LEVEL="INFO"

# you may wish to add these options for Celery Beat
CELERYBEAT_PID_FILE="/var/run/celery/beat.pid"
CELERYBEAT_LOG_FILE="/var/log/celery/beat.log"
```

### Celery Beat Service

- `usr/lib/systemd/system/celerybeat.service`

```ini
[Unit]
Description=Celery Beat Service
After=network.target

[Service]
Type=simple
# User=celery
# Group=celery
EnvironmentFile=/etc/conf.d/celery
WorkingDirectory=/data/app/proj
ExecStart=/bin/sh -c '${CELERY_BIN} beat \
  -A ${CELERY_APP} --pidfile=${CELERYBEAT_PID_FILE} \
  --logfile=${CELERYBEAT_LOG_FILE} --loglevel=${CELERYD_LOG_LEVEL}'

[Install]
WantedBy=multi-user.target
```

### Celery Worker Service

- `usr/lib/systemd/system/celery.service`

```ini
[Unit]
Description=Celery Service
After=network.target

[Service]
Type=forking
# User=celery
# Group=celery
EnvironmentFile=/etc/conf.d/celery
WorkingDirectory=/data/app/proj
ExecStart=/bin/sh -c '${CELERY_BIN} multi start ${CELERYD_NODES} \
  -A ${CELERY_APP} --pidfile=${CELERYD_PID_FILE} \
  --logfile=${CELERYD_LOG_FILE} --loglevel=${CELERYD_LOG_LEVEL} ${CELERYD_OPTS}'
ExecStop=/bin/sh -c '${CELERY_BIN} multi stopwait ${CELERYD_NODES} \
  --pidfile=${CELERYD_PID_FILE}'
ExecReload=/bin/sh -c '${CELERY_BIN} multi restart ${CELERYD_NODES} \
  -A ${CELERY_APP} --pidfile=${CELERYD_PID_FILE} \
  --logfile=${CELERYD_LOG_FILE} --loglevel=${CELERYD_LOG_LEVEL} ${CELERYD_OPTS}'

[Install]
WantedBy=multi-user.target
```