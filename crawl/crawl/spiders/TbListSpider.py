# -*- coding: utf-8 -*-
import scrapy
import sys
import json
import time
from crawl.items import GetListItem
import urlparse
class TbListSpider(scrapy.Spider):
    name = "tblistspider"
    allowed_domains = ["taobao.com"]
    start_urls = (
        'https://hstar-hi.alicdn.com/dream/ajax/getProjectList.htm?pageSize=64&projectType=&type=6&status=3&sort=5',    )

    def parse(self, response):
    	item = GetListItem()
        getjson = json.loads(response.body_as_unicode())
        for x in getjson['data']:
            for y in x:
                print y,':',x[y]

            item["id"] = x['id']
            item["name"] = x['name']
            #match = pattern.match(x['image'])
            #print match.group()
            item["thumbnail"] = x['image'].split('/')[-1]
            item["source"] = "https://izhongchou.taobao.com/dream/ajax/getProjectForDetail.htm?id="+x['id']
            item["website"] = "taobao"
            item["time"] = time.strftime("%Y-%m-%d %H:%M %p", time.localtime())
            item['image_urls'] =['http:'+x['image']]
            #item['images']

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
            '''
            yield item