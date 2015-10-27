#item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import sqlite3
from os import path
import os
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
import re
#from scrapy.pipelines.images.ImagesPipeline import ImagesPipeline
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy import log

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

class ThumbNailImagesPipeline(ImagesPipeline):
    #def file_path(self, request, response=None, info=None):
    #    image_guid = request.url.split('/')[-1]
    #    return 'full/%s' % (image_guid)
    id = ''
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)
        self.id = item['id']
                            
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        #if item['id']:
        #    newname = 'tb_' + item['id'] + '.jpg'
        #print 'image_paths:',image_paths[0]
        #os.rename(os.getcwd()+'/../img/'+image_paths[0],os.getcwd()+'/../img/thumbnail/'+newname)
        #os.mkdir("/tmp/1")
        #os.rename(image_paths[0], "./img/thumbnail/" + newname)
        return item
    def file_path(self, request, response=None, info=None):
        #open("../img/image_urls.txt","a").write(request.url + "\n")
        image_guid = request.url.split('/')[-1]
        return 'thumbnail/%s' % (image_guid)