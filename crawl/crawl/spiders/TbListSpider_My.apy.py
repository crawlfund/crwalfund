# -*- coding: utf-8 -*-
import scrapy
import sys;
from crawl.items import CrawlFundItem
import json;

class TbListSpider(scrapy.Spider):
    name = "tblistspider"
    allowed_domains = ["taobao.com"]
    start_urls = (
        'https://izhongchou.taobao.com/dream/ajax/getProjectList.htm?page=1&pageSize=10000&projectType=&type=6&status=3&sort=5',    )

    def parse(self, response):
        item = CrawlFundItem()
        getjson=json.loads(response.body_as_unicode(),encoding='utf-8')
        for x in getjson['data']:
            for y in x:
                print y,':',x[y]
