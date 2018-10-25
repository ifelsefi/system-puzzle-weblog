# Insight DevOps Engineering System Puzzle: Weblog - Solution

[Original Code](https://github.com/InsightDataScience/System-Puzzle-Weblog)


# Solution #

## docker-compose.yml ##
`db` did not have port mapping defined so it was difficult to check whether it was being populated properly.  So I exposed host port `5432` to the same container port

`nginx` was set to listen on host port `80,` which would be the same as `ingestion` service so I changed that to 8080.  Moreover, it was set to use container port `8080` which isn't correct given `conf.d/flaskapp.conf`

## All Python Applications ##

All `requirements` had psycopg2-binary added per [upcoming changes](http://initd.org/psycopg/articles/2018/02/08/psycopg-274-released/)

Remove several blank lines that contained whitespaces in all Python application files as well as those which were too long.

## Ingestion Application ##

Dockerfile did not copy over `utils.py.`

Added `source` to `body` var which will store the source in RabbitMQ.

## Processing Application ## 

Split `values` var into two others `v1` and `v2` then added another `v3` which contains `source.`

## FlaskApp ##

Created two variables `local_sql_success` and `remote_sql_success` which pull from the `source` column in postgres.

These values are then converted to a percent then printed on a separate line in `templates/index.html.`

