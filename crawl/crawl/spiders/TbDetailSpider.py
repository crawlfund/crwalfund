# -*- coding: utf-8 -*-
import scrapy
import sys
import json
import time
from crawl.items import GetDetailItem
import sqlite3
from os import path
import string

class TbDetailSpider(scrapy.Spider):
    #use this pipeline
    pipelines = ['crawl.pipelines.SqliteStoreDetailPipeLine']
    
    name = "tbdetailspider"
    allowed_domains = ["taobao.com"]
    start_urls = [
        'https://www.taobao.com',    ]
    #Use class construct function to generate start_urls
    def __init__(self, *args, **kwargs):
        request_urls = 'https://izhongchou.taobao.com/dream/ajax/getProjectForDetail.htm?id='
        conDB = GetlistfromDB()
        conDB.openDB()
        project_id_list = conDB.loadProjectIDList()
        for i,x in enumerate(project_id_list):
            self.start_urls.append(request_urls+x[0])
            print 'process:',self.start_urls[i]
        #self.start_urls = self.link
        conDB.closeDB()

    def parse(self, response):
    	item = GetDetailItem()
        getjson = json.loads(response.body_as_unicode())
        for x in getjson['data']:
                
            '''
            item["time"] = time.strftime("%Y-%m-%d %H:%M %p", time.localtime())
            item["id"] = x['id']
            item["name"] = x['name']
            item["image"] = x['image']
            item["curr_money"] = x['curr_money']
            item["buy_amount"] = x['buy_amount']
            item["remain_day"] = x['remain_day']
            item["status"] = x['status']
            item["target_money"] = x['target_money']
            item["focus_count"] = x['focus_count']
            item["plan_date"] = x['plan_date']
            item["plan_end_date"] = x['plan_end_date']
            yield item
            '''
class GetlistfromDB:
    filename = 'project.db'
    def openDB(self):
        self.conn=None
        if path.exists(self.filename):
            self.conn=sqlite3.connect(self.filename)
        else:
            #To do: add error log message
            log.msg("Database not found!", level=log.ERROR)
    def loadProjectIDList(self,):
        cursor = self.conn.cursor()
        cursor.execute('select DISTINCT id from projectlist')
        result = cursor.fetchall()
        return result
    def closeDB(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn=None