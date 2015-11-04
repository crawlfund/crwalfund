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
    name = scrapy.Field()
    image = scrapy.Field()
    #开始众筹日期
    begin_date = scrapy.Field()
    #结束日期
    end_date = scrapy.Field()
    #卖家名称
    nick = scrapy.Field()
    #目标金额
    target_money = scrapy.Field()
    #支持人数
    support_person = scrapy.Field()
    #已筹集金额
    curr_money = scrapy.Field()
    #完成比例
    finish_per = scrapy.Field()
    #剩余时间
    remain_day = scrapy.Field()
    #状态
    status = scrapy.Field()
    #预热开始七日
    plan_date = scrapy.Field()
    #预热结束日期
    plan_end_date = scrapy.Field()
    #描述
    desc = scrapy.Field()
    #内容？
    content = scrapy.Field()
    #视频地址
    video = scrapy.Field()
    #QR码(二维码)
    qrcode = scrapy.Field()


class TumbNailItem(scrapy.Item):
    #项目id后来采集数据需要用到
    image_urls = scrapy.Field()
    #项目名称
    images = scrapy.Field()