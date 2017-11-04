# coding:utf8
import urllib
import urllib2
import json


def not1(key):
    dase_url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'

    data = {
        'type': 'AUTO',
        'i': key,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'ue': 'UTF-8',
        'typoResult': 'true',
        "action": "FY_BY_CLICKBUTTON",
    }
    ua_list = {
        'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
    }
    data = urllib.urlencode(data)

    request = urllib2.Request(dase_url, data=data)
    response = urllib2.urlopen(request)

    data_json = response.read()
    data = json.loads(data_json)
    print data
    exit()
    request.add_header('User-Agent', ua_list)

    target = data["translateResult"][0][0]['tgt']
    print target

    result = data['smartResult']['entries']
    result_str = '\n'.join(result[1:])  # result列表中第一个元素
    print result_str

if __name__ == '__main__':
    while True:
        key = raw_input('请输入要翻译的单词:')
        if key == 'q':
            exit()
        else:
            not1(key)
