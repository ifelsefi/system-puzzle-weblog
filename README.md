# Insight DevOps Engineering System Puzzle: Weblog - Solution

[Original Code](https://github.com/InsightDataScience/System-Puzzle-Weblog)


# Solution #

## docker-compose.yml ##

Changes were made to properly expose host to containers.

## All Python Applications ##

All `requirements` had psycopg2-binary added per [upcoming changes](http://initd.org/psycopg/articles/2018/02/08/psycopg-274-released/)

Remove several blank lines that contained whitespaces as well as those which were too long.

## Postgres ##

No longer stopping on `psql` errors.

Added column for `source`.

## Ingestion Application ##

`utils.py` no longer absent.

Now storing `source` in RabbitMQ.

## Processing Application ## 

Now writing `source` to Postgres.

## Flask Application ##

Created two variables `local_sql_success` and `remote_sql_success` which pull from the `source` column in Postgres.

These values are then converted to a percent then printed on a separate line in `templates/index.html.`

# TODO #

Add more exception handling to all Python applications
