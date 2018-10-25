# below isn't used
# import datetime
import os
import psycopg2

from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']


# need two blank lines
@app.route("/", methods=('GET', 'POST'))
def index():
    # Connect to database
    # fixed line too long [e501]
    conn = psycopg2.connect(host='db', database=os.environ['POSTGRES_DB'],
                            user=os.environ['POSTGRES_USER'],
                            password=os.environ['POSTGRES_PASSWORD'])
    cur = conn.cursor()

    # Get number of all GET requests
    sql_all = """SELECT COUNT(*) FROM weblogs;"""
    cur.execute(sql_all)
    all = cur.fetchone()[0]

    # Get number of local succesful requests
    local_sql_success = """SELECT COUNT(*) FROM weblogs WHERE status
                           LIKE \'2__\' AND source LIKE \'local\';"""
    cur.execute(local_sql_success)
    local_success = cur.fetchone()[0]

    remote_sql_success = """SELECT COUNT(*) FROM weblogs WHERE status
                           LIKE \'2__\' AND source LIKE \'remote\';"""
    cur.execute(remote_sql_success)
    remote_success = cur.fetchone()[0]

    # Determine rate if there was at least one request
    local_rate = "No local entries yet!"
    remote_rate = "No remote entries yet!"
    if all != 0:
        # converting both to round numbers
        local_rate = round(local_success / all * 100)
        remote_rate = round(remote_success / all * 100)

    # fixed [e251] error
    return render_template('index.html', local_rate=local_rate,
                           remote_rate=remote_rate)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
