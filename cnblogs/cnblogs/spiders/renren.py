# -*- coding: utf-8 -*-
import scrapy

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    #start_urls = ['http://www.renren.com/SysHome.do']

    def start_requests(self):
        login_url = 'http://www.renren.com/PLogin.do'
        data = {
            "email":'1752570559@qq.com',
            "password'":'1234qwer',
        }
        yield scrapy.FormRequest(url=login_url, formdata=data, callback=self.after_login)

    def after_login(self, response):
        print "222222222222222222222222222222"
        print response.body
#
# class Renren2Spider(scrapy.Spider):
#     name = 'renren2'
#     allowed_domains = ['renren.com']
#
#     def start_requests(self):
#         login_url = 'http://www.renren.com/PLogin.do'
#         # 发送post请求
#         data = {
#             "email": '1752570559@qq.com',
#             "password": '1234qwer',
#         }
#         yield scrapy.FormRequest(url=login_url, formdata=data, callback=self.after_login)
#
#     # 登陆以后处理
#     def after_login(self, response):
#         print response.body
