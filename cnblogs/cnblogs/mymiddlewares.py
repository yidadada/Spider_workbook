# -*- coding: utf-8 -*-

from settings import USER_AGENS,PROXY_IP #导入指定值，使用时直接使用值
import random
import base64
from scrapy.conf import settings #导入使用的是settings['值]，
#import settings 使用的话是引用，settings.(值)，相当于引用了一个settings模块

class RandomUserAgent(object):
    def process_request(self,request,spider):
        user_agent = random.choice(USER_AGENS)
        request.headers.setdefault('User-Agent', user_agent)

class RandomIP(object):
    def process_request(self,request,spider):  #每个request通过下载中间件时，该方法被调用
        IP_LIST = random.choice(PROXY_IP)
        if IP_LIST.get('auth') is None:  #免费代理
            request.meta['proxy'] = "http://" + IP_LIST['host']
            print "++++++++++++++++++++"
        else:
            auth = base64.b64encode(IP_LIST['auth'])
            request.headers['Proxy-Authorization'] = 'Basic ' + auth
            request.meta['proxy'] = 'http://' + IP_LIST['host']
            print "_______________________________"

class RandomKuaiDai(object):

    def process_request(self,request,spider):
        ip_list = random.choice(settings['PROXIES'])

        if ip_list.get('auth') is None:
            print ("?"*100)
            print ip_list['id_list']
            request.meta['proxy'] = "http://"+ip_list['id_list']+":"+ip_list['port']





