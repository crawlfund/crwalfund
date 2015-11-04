# all the imports

from flask.ext.pymongo import PyMongo
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import json

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
    a = mongo.db.tblist_items.distinct("id")
    project = mongo.db.tblist_items.find()
    return render_template('index.html',entries=project)

@app.route('/detail/')
def show_detail():
    a = mongo.db.tblist_items.distinct("id")
    project = mongo.db.tblist_items.find()
    return render_template('detail.html',entries=project)

@app.route('/ajax/request', methods=['GET'])
def detail2json():
    if request.method == 'GET':
        id = int(request.args.get('id', 10))
        #tag = int(request.args.get('tag'),0)
        #count = int(request.args.get('count'),0)
        results = mongo.db['tblist_items'].distinct("id")#.limit(count)
        json_results= []
        for result in results:
            json_results.append(result)
        print results
        return json.dumps(json_results)

@app.teardown_request
def teardown_request(exception):
    pass


if __name__ == '__main__':
    app.run()