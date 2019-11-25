#!/bin/bash

mkdir -p /logs/input_jd
mkdir -p /logs/output_jsp
mkdir -p /logs/output_humanreadable
mkdir -p /logs/output_jsphr

MAX_RETRIES=50
RETRIES=0

echo "Waiting for database connection..."
until python ./jdxapi/wait_for_db.py; do
    RETRIES=`expr $RETRIES + 1`
    if [[ "$RETRIES" -eq "$MAX_RETRIES" ]]; then
        echo "Retry Limit Exceeded. Aborting..."
        exit 1
    fi
    sleep 2
done


# if [ "$APP_ENV" == "DEVELOPMENT" ] || [ -z "$APP_ENV" ]; then
# else
#     gunicorn -b 0.0.0.0 jdxapi.app:app
# fi

# --timeout 240
gunicorn -b 0.0.0.0 --workers=1 jdxapi.app:app --worker-class gevent --log-level debug --access-logfile -