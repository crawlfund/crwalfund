# -*- coding: utf-8 -*-
import scrapy
import sys
import json
import time
from crawl.items import TumbNailItem
from scrapy.selector import Selector
import urlparse

class TestImageSpider(scrapy.Spider):
    name = "testimage"
    allowed_domains = ["blu-raydisc.tv"]
    start_urls = ('http://blu-raydisc.tv/',)
    def parse(self, response):
        sel = Selector(response)
        item = TumbNailItem()
        item['image_urls'] = [ urlparse.urljoin(response.url, u) for u in sel.xpath('//img/@src').extract()]
        #        item['image_urls'] = sel.xpath('//img/@src').re(r'.*[jpg|gif|png]$')
        #item['images'] = sel.xpath('//img/@src').re(r'[^/]*.[jpg|png|gif]$')
        #        [os.system('wget %s' %i) for i in item['image_urls']]   我们上面启用了下载管道，这句话就不科学了 果断注释掉
        return item
        #yield item