# all the imports

from flask.ext.pymongo import PyMongo
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash


# configuration

DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'items'
mongo = PyMongo(app, config_prefix='MONGO')
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.before_request
def before_request():
    pass


@app.route('/')
def show_entries():
    project = mongo.db.tblist_items.find()
    return render_template('index.html',entries=project)

@app.teardown_request
def teardown_request(exception):
    pass


if __name__ == '__main__':
    app.run()