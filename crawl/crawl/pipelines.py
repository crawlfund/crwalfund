#item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import sqlite3
from os import path
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
import re
class SqlitePipeLine(object):
    filename = 'taobao.db'
    def __init__(self):
        self.conn=None
        dispatcher.connect(self.initialize,signals.engine_started)
        dispatcher.connect(self.finalize,signals.engine_stopped)
    def process_item(self,item,spider):
        self.conn.execute('insert into projectlist values(?,?,?,?)',(None,item['title'][0],'http://www.fjsen.com/'+item['link'][0],item['addtime'][0]))
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
        conn.execute("""create table projectlist (id integer primary key autoincrement,title text,link text,addtime text)""")
        conn.commit()
        return conn

class SqliteStoreListPipeLine(object):
    filename = 'project_list.db'
    def __init__(self):
        self.conn=None
        dispatcher.connect(self.initialize,signals.engine_started)
        dispatcher.connect(self.finalize,signals.engine_stopped)
    def process_item(self,item,spider):
        self.conn.execute('insert into projectlist values(?,?,?,?,?,?,?,?,?,?,?)',(item['id'][0],'http://www.fjsen.com/'+item['name'][0],item['image'][0],item['curr_money'][0],item['buy_amount'][0],item['remain_day'][0],item['status'][0],item['target_money'][0],item['focus_count'][0],item['plan_date'][0],item['plan_end_date'][0]))
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
        conn.execute("""create table projectlist (id integer primary key NOT NULL,name text,image text,curr_money text,buy_amount text,remain_day text,status text,target_money text,focus_count text,plan_date text,plan_end_date text)""")
        conn.commit()
        return conn
