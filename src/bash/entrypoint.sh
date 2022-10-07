#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

if [[ $RUNTYPE == 'CRON' ]]; then
  echo 'RUNNING APP IN CRON MODE'
  echo "RUNNING $1 $2 $3 $4"
  $1 $2 $3 $4
  exit $?
else
  echo 'RUNNING APP IN NORMAL MODE'
  nginx && \
  gunicorn --access-logfile "-" --error-logfile "-" -w 1 wsgi:app
fi