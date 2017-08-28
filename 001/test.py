#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

#设定访问的入口网址:使用孔夫子旧书网做参考
entry = 'http://www.kongfz.com/'
#请求头文件设定
file = 'header.txt'
#用于保存链接的set
links = set()

#通过header.txt载入用于设置request的header
def load_header(filename):
    header = {}
    with open(filename) as file:
        for line in file:
            key,value = line.rstrip().split(':', maxsplit=1)
            header[key] = value
    return header

###################################################################
#测试是否不需要修改ug头而且不需要cookies就可以访问
# resp = requests.get(entry)
# resp.raise_for_status()
#结论：不能访问
###################################################################

###################################################################
#测试修改ug头后是否可以访问
# #获取ug头
ug = load_header('header.txt')
#设置ug并访问网站
resp = requests.get(entry, headers=ug)
# resp.raise_for_status()
#结论：网站通过ug控制了用户的访问
###################################################################

###################################################################
#使用BeautifulSoup解析网站获取所有的连接对象
resp.encoding = 'utf-8'
bsobj = BeautifulSoup(resp.text, 'html.parser')
#查找所有的a标签
tags = bsobj.find_all('a')
print(len(tags))
#遍历a标签
for tag in tags:
    if 'href' in tag.attrs:
        #使用regex剔除所有的外链
        p = re.compile(r'http.*kongfz.*')
        m = p.match(tag['href'])
        #如果匹配
        if m:
            #向links添加连接
            links.add(m.group())
            print(m.group())
        else:
            continue

























