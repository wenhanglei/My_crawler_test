import requests

#指定需要爬取的url
url = 'https://www.wikipedia.org/wiki/Main_Page'

#获得response对象
resp = requests.get(url)

#设定response的编码为utf-8
resp.encoding = 'utf-8'
#获得响应文本
resp.text

#获得response对象的响应头
# headers = resp.headers

#打印响应头内容
# for (key, value) in headers.items():
#     print(key + ': ' + value)