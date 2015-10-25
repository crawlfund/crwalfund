# -*- coding: utf-8 -*-
import scrapy
import sys
import json
import time
from crawl.items import GetListItem

class TbListSpider(scrapy.Spider):
    name = "tblistspider"
    allowed_domains = ["taobao.com"]
    start_urls = (
        'https://izhongchou.taobao.com/dream/ajax/getProjectList.htm?page=1&pageSize=10000&projectType=&type=6&status=3&sort=5',    )

    def parse(self, response):
    	item = GetListItem()
        getjson = json.loads(response.body_as_unicode())
        for x in getjson['data']:
            print x['id'],x['name'],x['image'],x['curr_money'],x['buy_amount'],\
            x['remain_day'],x['status'],x['target_money'],x['focus_count'],\
            x['plan_date'],x['plan_end_date']

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
