# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import MySQLdb
import pymongo
from scrapy.conf import settings

class Py02ScrapyDay11Pipeline(object):
    def process_item(self, item, spider):
        return item

#写入json
class cnblogs(object):
    def __init__(self):
        self.f = open('cnblogs.json','w')

    def process_item(self,item,spider):
        self.f.write(json.dumps(dict(item), ensure_ascii=False).encode('utf-8') + '\n')
        return item

    def close_spider(self,spider):
        self.f.close()

#写入数据库
class MySQLdbpilines(object):
    # 初始化
    def __init__(self):
        try:
            self.conn = MySQLdb.connect('192.168.2.134', 'mayinan', '123456', 'myweb', charset='utf8')
            self.cursor = self.conn.cursor()
        except Exception, e:
            print '数据库连接失败'
            print str(e)

    def process_item(self,item,spider):
        sql = 'insert into cnblogs(detail,title,url,jianjie,author,comment_num,view_num,shijian) ' \
              'values(%s,%s,%s,%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(sql,(
            item['detail'], item['title'], item['url'], item['jianjie'], item['author'], item['comment_num'],
            item['view_num'], item['shijian']))
            self.conn.commit()
        except Exception, e:
            print '插入失败', str(e)
        return item

    def close(self):
        self.cursor.close()
        self.conn.close()

class TencentMySQLdbpilines(object):
    def __init__(self):
        try:
            self.conn = MySQLdb.connect('192.168.2.134','mayinan','123456','myweb',charset = 'utf8')
            self.cursor =self.conn.cursor()
        except:
            print '####wrong#################################################################################'

    def process_item(self,item ,spider):
        sql = 'insert into tencent(title,location,type,num)' \
              'values(%s,%s,%s,%s)'
        try:
            self.cursor.execute(sql,(item['title'], item['location'], item['type'], item['num']))
            #数据得值应该是一个元组或者列表
            self.conn.commit()
        except Exception, e:
            print '插入失败', str(e)
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

#写入json
class Tencentpilines(object):

    def __init__(self):
        self.f = open('tencent.json','a')

    def process_item(self,item,spider):
        self.f.write(json.dumps(dict(item),ensure_ascii = False).encode('utf-8') + '\n')
    def close_spider(self,spider):
        print 'file has been closed%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
        self.f.close()

#xici写入json
class Xicipilines(object):
    def __init__(self):
        self.f = open('xici.json','w')

    def process_item(self,item,spider):
        self.f.write(json.dumps(dict(item),ensure_ascii= False).encode('utf-8') + '\n')

    def close_spider(self,spider):
        self.f.close()

#xici写入mongodb
class rootPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(settings['MONGO_HOST'],settings['MONGO_PORT'])

    def process_item(self, item, spider):
        #print dict(item)
        data = self.client[settings['MONGODB_DBNAME']]
        dict_item = dict(item)
        data.text.insert(dict_item)
        return item

