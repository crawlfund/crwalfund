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

@app.route('/detail/<site>/<id>')
def show_detail(site,id):
    project = mongo.db.tblist_items.find({'id':id},{'_id':0,'id':1,'name':1,'thumbnail':1,'website':1}).limit(1)
    detail = mongo.db.tbdetail_items.find({'id':id}).sort({})
    for result in project:
        print result
    return render_template('detail.html',entries=result)

@app.route('/ajax/getlist', methods=['GET'])
def get_list():
    if request.method == 'GET':
        id = int(request.args.get('id', 10))
        tag = int(request.args.get('tag',10))
        count = int(request.args.get('count',10))
        if count > 100:
            count = 100
        results = mongo.db['tblist_items'].find({'website':'taobao'},{'_id':0,'id':1,'name':1,'thumbnail':1,'website':1}).limit(count)
        print results.count()
        datalist= []
        json_results={}
        for result in results:
            datalist.append(result)
        #print datalist
        return json.dumps(datalist)


@app.teardown_request
def teardown_request(exception):
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9091)
