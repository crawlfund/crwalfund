# -*- coding: utf-8 -*-
import scrapy
import sys;
from crawl.items import CrawlFundItem


class TestpipelineSpider(scrapy.Spider):
    name = "testpipeline"
    allowed_domains = ["wellmakers.com"]
    start_urls = (
        'http://www.wellmakers.com/',
    )

    def parse(self, response):
	item = CrawlFundItem()
	for x in range(3):
	    item['title'] = 'hello world'
            item['link']  = 'some link'
	    item['addtime']  = 'time'
	yield item	
        
