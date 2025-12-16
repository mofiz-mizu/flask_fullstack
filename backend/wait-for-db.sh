#!/bin/sh
echo "Waiting for db..."
while ! mysqladmin ping -h"$DB_HOST" -u"$DB_USER" -p"$DB_PASSWORD" --silent; do
  sleep 2
done
echo "Database is ready!"
exec "$@"
