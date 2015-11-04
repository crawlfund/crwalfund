# -*- coding: utf-8 -*-
import scrapy
import sys
import json
import time
import string
from pymongo import MongoClient
from crawl.items import GetDetailItem
from os import path


class TbDetailSpider(scrapy.Spider):
    #use this pipeline
    pipelines = ['crawl.pipelines.SqliteStoreDetailPipeLine']    
    name = "tbdetailspider"
    allowed_domains = ["taobao.com"]
    start_urls = []

    #Use class construct function to generate start_urls

    def __init__(self, *args, **kwargs):
        request_urls = 'https://izhongchou.taobao.com/dream/ajax/getProjectForDetail.htm?id='
        client = MongoClient()
        #MongoClient("mongodb://127.0.0.1:27019")
        db = client.items
        cursor = db.tblist_items.distinct("id")
        for i,x in enumerate(cursor):
            self.start_urls.append(request_urls+x)


    def parse(self, response):
    	item = GetDetailItem()
        getjson = json.loads(response.body_as_unicode())
        for x in getjson['data']:
            item["name"] = x['name']
            item["image"] = x['image']
            item["begin_date"] = x['begin_date']
            item["end_date"] = x['end_date']
            item["nick"] = x['nick']
            item["target_money"] = x['target_money']
            item["support_person"] = x['support_person']
            item["curr_money"] = x['curr_money']
            item["finish_per"] = x['finish_per']
            item["remain_day"] = x['remain_day']
            item["status"] = x['status']
            item["plan_date"] = x['plan_date']
            item["plan_end_date"] = x['plan_end_date']
            item["desc"] = x['desc']
            item["content"] = x['content']
            item["video"] = x['video']
            item["qrcode"] = x['qrcode']
            yield item
