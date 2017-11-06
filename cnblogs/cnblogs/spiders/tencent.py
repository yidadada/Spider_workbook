# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from cnblogs.items import tencentitem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php']

    rules = (
        Rule(LinkExtractor(allow=(r'position_detail',)),callback='parse_item',follow=True,),
        #Rule(LinkExtractor(allow=(r'start=\d+',)),follow=True),
    )

    def parse_item(self, response):
        #print response.url
        item = tencentitem()
        item['title']= response.xpath('//table[@class="tablelist textl"]//tr[@class="h"]/td/text()').extract()[0]
        item['location'] = response.xpath('//table[@class="tablelist textl"]//tr[@class="c bottomline"]/td[1]/text()').extract()[0]
        item['type'] = response.xpath('//table[@class="tablelist textl"]//tr[@class="c bottomline"]/td[2]/text()').extract()[0]
        item['num'] = response.xpath('//table[@class="tablelist textl"]//tr[@class="c bottomline"]/td[3]/text()').extract()[0]
        #item['zhize'] = response.xpath('//table[@class="tablelist textl"]//tr[3]').extract()[0]
        #item['yaoqiu'] = response.xpath('//table[@class="tablelist textl"]//tr[4]').extract()[0]
        yield item

    def link_chuli(self,links):
        for link in links:
            link.url = link.url.replace('position.php/','')
        return links

    #rute规则中加入 process_links='link_chuli'，可以处理抓取出的url地址