# -*- coding: utf-8 -*-
import scrapy
from cnblogs.items import xici

class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    # page = 1
    # basic_url = 'http://www.kuaidaili.com/free/intr/%d'
    # start_urls = [basic_url %page]

    def start_requests(self):
        basic_url = 'http://www.kuaidaili.com/free/intr/%d'
        for i in range(1,2):
            fullurl = basic_url %i
            yield scrapy.Request(fullurl,callback = self.parse)

    def parse(self, response):
        id_list = response.xpath('//tr')[1:]
        for ipp in id_list:
            item = xici()
            item['id_list'] = ipp.xpath('.//td[1]/text()').extract()[0]
            item['port'] = ipp.xpath('.//td[2]/text()').extract()[0]
            item['id_type'] = ipp.xpath('.//td[4]/text()').extract()[0]
            item['location'] = ipp.xpath('.//td[5]/text()').extract()[0]
            item['speed'] =ipp.xpath('.//td[6]/text()').extract()[0]
            item['update_time'] = ipp.xpath('.//td[7]/text()').extract()[0]
            yield item

        # while self.page <10:
        #     self.page += 1
        #     yield scrapy.Request(self.basic_url % self.page ,callback = self.parse)




