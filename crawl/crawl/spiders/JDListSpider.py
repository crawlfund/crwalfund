# -*- coding: utf-8 -*-
import scrapy
import sys
import json
import time
from crawl.items import GetListItem
import urlparse
class TbListSpider(scrapy.Spider):
    name = "jdlistspider"
    allowed_domains = ["jd.com"]
    start_urls = [
                  'http://z.jd.com/bigger/get_choose_home.action?pageNo=1&sceneEnd=0&productEnd=0&state=1&sort=jjks&_=1446482753023',    ]
    #Use class construct function to generate start_urls
    def __init__(self, *args, **kwargs):
        request_urls = 'http://z.jd.com/bigger/get_choose_home.action?pageNo=1&sceneEnd=0&productEnd=0&state=1&sort=jjks&_='
        num_13 = '%d' % time.time()
        print num_13
        for i in range(1000):
            num_3 = '%d' % i
            num=str(num_13)+str(num_3)
            self.start_urls.append(request_urls+num)
            print 'process:',self.start_urls[i]
    def parse(self, response):
        #item = GetListItem()
        f = file('poem.txt','a')
        f.write(response.body)
        f.close()
        try:
            getjson = json.loads(response.body_as_unicode())
        except:
            pass

        #redirects = request.meta.get('redirect_times', 0) + 1