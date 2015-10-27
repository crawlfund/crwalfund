# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetListItem(scrapy.Item):
    #项目id后来采集数据需要用到
    id = scrapy.Field()
    #项目名称
    name = scrapy.Field()
    #缩略图
    thumbnail = scrapy.Field()
    #目标项目链接
    source = scrapy.Field()
    #抓取时间
    time = scrapy.Field()
    #来源网站
    website = scrapy.Field()

    image_urls = scrapy.Field()
#images =scrapy.Field()
class GetDetailItem(scrapy.Item):
    #项目id后来采集数据需要用到
    id = scrapy.Field()
    #项目名称
    name = scrapy.Field()
    #图片地址
    image = scrapy.Field()
    #当前筹集到的
    curr_money = scrapy.Field()
    #购买人数
    buy_amount = scrapy.Field()
    #剩余开始天数
    remain_day = scrapy.Field()
    #目前状态
    status = scrapy.Field()
    #目标金额
    target_money = scrapy.Field()
    #喜欢人数
    focus_count = scrapy.Field()
    #计划开始时间
    plan_date = scrapy.Field()
    #计划结束时间
    plan_end_date = scrapy.Field()
    #抓取时间
    time =scrapy.Field()
class TumbNailItem(scrapy.Item):
    #项目id后来采集数据需要用到
    image_urls = scrapy.Field()
    #项目名称
    images = scrapy.Field()