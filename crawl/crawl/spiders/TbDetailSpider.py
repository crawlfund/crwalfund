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
    name = 'tbdetailspider'
    allowed_domains = ['taobao.com']
    start_urls = []

    #Use class construct function to generate start_urls

    def __init__(self, *args, **kwargs):
        request_urls = 'https://izhongchou.taobao.com/dream/ajax/getProjectForDetail.htm?id='
        client = MongoClient()
        #MongoClient('mongodb://127.0.0.1:27019')
        db = client.items
        cursor = db.tblist_items.distinct('id')
        for i,x in enumerate(cursor):
            self.start_urls.append(request_urls+x)


    def parse(self, response):
    	item = GetDetailItem()
        getjson = json.loads(response.body_as_unicode())

        item['name'] = getjson['data']['name']
        item['image_detail'] = getjson['data']['image']
        item['begin_date'] = getjson['data']['begin_date']
        item['end_date'] = getjson['data']['end_date']
        item['nick'] = getjson['data']['nick']
        item['target_money'] = getjson['data']['target_money']
        item['support_person'] = getjson['data']['support_person']
        item['curr_money'] = getjson['data']['curr_money']
        item['finish_per'] = getjson['data']['finish_per']
        item['remain_day'] = getjson['data']['remain_day']
        item['status'] = getjson['data']['status']
        item['plan_date'] = getjson['data']['plan_date']
        item['plan_end_date'] = getjson['data']['plan_end_date']
        item['desc'] = getjson['data']['desc']
        item['content'] = getjson['data']['content']
        item['video'] = getjson['data']['video']
        item['qrcode'] = getjson['data']['qrcode']
        yield item
