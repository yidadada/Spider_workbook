import pymongo
client = pymongo.MongoClient("101.132.157.111",27017)
data = client['d1']
data.host.insert({'host':'192.168.1.1'})

