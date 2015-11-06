#item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
#import sqlite3

import os
import re
import pymongo
from os import path
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy import log
#from scrapy.pipelines.images.ImagesPipeline import ImagesPipeline

class MongoListPipeline(object):

    collection_name = 'tblist_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('mongodb://127.0.0.1:27019'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if spider.name not in ['tblistspider']:
            return item
        self.db[self.collection_name].insert(dict(item))
        return item

class MongoDetailPipeline(object):

    collection_name = 'tbdetail_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('mongodb://127.0.0.1:27019'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        print spider.name
        if spider.name not in ['tbdetailspider']:
            return item
        self.db[self.collection_name].insert(dict(item))
        return item

class ThumbNailImagesPipeline(ImagesPipeline):

    #def file_path(self, request, response=None, info=None):
    #    image_guid = request.url.split('/')[-1]
    #    return 'full/%s' % (image_guid)
    id = ''
    def get_media_requests(self, item, info):
        try:
            for image_url in item['image_urls']:
                yield Request(image_url)
            self.id = item['id']
        except:
            pass
    
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item
    def file_path(self, request, response=None, info=None):
        #open("../img/image_urls.txt","a").write(request.url + "\n")
        image_guid = request.url.split('/')[-1]
        return 'thumbnail/%s' % (image_guid)

'''
class SqliteStoreDetailPipeLine(object):
    filename = 'project.db'
    def __init__(self):
        self.conn=None
        dispatcher.connect(self.initialize,signals.engine_started)
        dispatcher.connect(self.finalize,signals.engine_stopped)
    def process_item(self,item,spider):
        #check pipeline if is for this spider else return
        if spider.name not in ['tbdetailspider']:
            return item
        self.conn.execute('insert into projectdetail values(?,?,?,?,?,?,?,?,?,?,?,?)',(item['id'],item['name'],item['image'],item['curr_money'],item['buy_amount'],item['remain_day'],item['status'],item['target_money'],item['focus_count'],item['plan_date'],item['plan_end_date'],item['time']))
        return item
    def initialize(self):
        if path.exists(self.filename):
            self.conn=sqlite3.connect(self.filename)
        else:
            self.conn=self.create_table(self.filename)
    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn=None
    def create_table(self,filename):
        conn=sqlite3.connect(filename)
        conn.execute("""create table projectdetail (id text primary key,name text,image text,curr_money text,buy_amount text,remain_day text,status text,target_money text,focus_count text,plan_date text,plan_end_date text,time text)""")
        conn.commit()
        return conn


class SqliteStoreListPipeLine(object):
    filename = 'project.db'
    def __init__(self):
        self.conn=None
        dispatcher.connect(self.initialize,signals.engine_started)
        dispatcher.connect(self.finalize,signals.engine_stopped)
    def process_item(self,item,spider):
        if spider.name not in ['tblistspider']:
            return item
        self.conn.execute('insert into projectlist values(?,?,?,?,?,?)',(item['id'],item['name'],item['thumbnail'],item['source'],item['website'],item['time']))
        return item
    def initialize(self):
        if path.exists(self.filename):
            self.conn=sqlite3.connect(self.filename)
        else:
            self.conn=self.create_table(self.filename)
    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn=None
    def create_table(self,filename):
        conn=sqlite3.connect(filename)
        conn.execute("""create table projectlist (id text,name text,thumbnail text,source text,time text,website text)""")
        conn.commit()
        return conn
'''