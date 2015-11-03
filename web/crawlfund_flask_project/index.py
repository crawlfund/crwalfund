# all the imports
import sqlite3
from flask import Flask
from flask.ext.pymongo import PyMongo
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
#For sqlite3
from contextlib import closing


# configuration
DATABASE = '../../crawl/crawl/spiders/project.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.before_request
def before_request():
    g.db = connect_db()

@app.route('/')
def show_entries():
    cur = g.db.execute('select DISTINCT * from projectlist')
    entries = [dict(id=row[0], name=row[1],thumbnail = row[2],source = row[3] ) for row in cur.fetchall()]
    return render_template('index.html', entries=entries)

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

if __name__ == '__main__':
    app.run()