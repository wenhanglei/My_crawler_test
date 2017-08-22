import requests
import request_header
from bs4 import BeautifulSoup
import shutil

#设置需要访问的登录页面
url = 'https://book.douban.com'


def change_cookies(cookiestr):
    li = cookiestr.split(';')
    cookies = {}
    for i in li:
        item = i.split("=")
        if item[1].startswith('"'):
            cookies[item[0]] = item[1][1:-2]
            # print('%s=%s' % (item[0], item[1][1:-1]))
        else:
            cookies[item[0]] = item[1]
            # print('%s=%s' % (item[0], item[1]))
    return cookies

#创建session对象
with requests.Session() as session:
    #设置session对象的请求头
    session.headers = request_header.header
    #转变cookie为可用的cookies
    cookies = change_cookies(cookiestr)
    #访问豆瓣登录页面获得返回响应页面
    resp = session.get(url, cookies = cookies)
    #保存返回的登录页面
    with open('douban.html', 'w', encoding='utf-8') as file:
        file.write(resp.text)
    for key, value in resp.cookies.items():
        print('%s=%s' % (key, value))







