#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util
from bs4 import BeautifulSoup
import re

#通过解析string获取时间信息
def get_min(st):
    regex = re.compile(r'(\d*) 分钟$')
    mc = regex.search(st)
    return mc.group(1)

#用于保存学习时间信息的list
data = []
#载入html
html = util.load_obj('html')
#构造beautifulSoup对象
bj = BeautifulSoup(html, 'html.parser')
#获取包含数据的容器
ctan = bj.find('div', id='checkin')
#获得所有的文本并打印
texts = ctan.find_all('div', class_='note')
for t in texts:
    #获取文本信息
    txt = t.string.strip()
    #使用正则表达式获取分钟时间数据
    minu = get_min(txt)
    #保存获取的时间数据
    data.append(int(minu))

sum = 0
for d in data:
    sum += d
thour = sum/60

print("你学习了%.2f小时" % round(thour))
