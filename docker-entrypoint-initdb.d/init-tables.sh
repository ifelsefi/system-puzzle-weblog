#!/bin/bash
set -e

# ls -ltr /var/lib/postgresql/data/
# cat /var/lib/postgresql/data/pg_hba.conf
# cat /var/lib/postgresql/data/postgresql.conf

# show env to ensure 'env_file' being sourced
# env

# username and database do not match 'env_file'
# added source so it can be displayed in flaskapp
psql -v ON_ERROR_STOP=0 --username $POSTGRES_USER --dbname $POSTGRES_DB <<-EOSQL
        CREATE TABLE  weblogs (
               day    date,
               status varchar(3),
               source varchar(6)
               );
EOSQL
