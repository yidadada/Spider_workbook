# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnblogsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class cnblogs(scrapy.Item):

    detail = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    #image_url= scrapy.Field()
    jianjie = scrapy.Field()
    author = scrapy.Field()
    comment_num  = scrapy.Field()
    view_num = scrapy.Field()
    shijian = scrapy.Field()

class tencentitem(scrapy.Item):

    title = scrapy.Field()
    location = scrapy.Field()
    type = scrapy.Field()
    num = scrapy.Field()
    #zhize = scrapy.Field()
    #yaoqiu = scrapy.Field()

class xici(scrapy.Item):

    id_list = scrapy.Field()
    port = scrapy.Field()
    location = scrapy.Field()
    id_type = scrapy.Field()
    update_time = scrapy.Field()
    speed = scrapy.Field()




