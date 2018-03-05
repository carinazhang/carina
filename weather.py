# -*- coding: utf-8 -*-
# __author__ = 'Carina'


from urllib.request import quote
from urllib.request import urlopen
from urllib.request import Request



url = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getSupportCity?byProvinceName='
# print(type(url))
#string1 = u'上海'.encode('utf-8')    # str编码会变成bytes
string = '上海'
string_code = quote(string)   # 对关键词部分编码
# print(string)
# print(type(string))
#string2 = ''
#print(type(string2))
url_all = url + string_code
# url_all=url % ("上海")
# print(url_all)
req = Request(url_all)
req.encoding='utf-8'
data = urlopen(req).readlines()
# print(type(data))
print(data)


'''
# 第二种方式，使用requests
import requests
from urllib.request import urlopen
from urllib.request import Request

param={"byProvinceName":"上海"}
response = requests.get("http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getSupportCity&quot;,params=param")
print(response.text)
'''


