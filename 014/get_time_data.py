#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from selenium import webdriver
import util
from bs4 import BeautifulSoup
import requests


#访问入口
entry = 'https://www.shanbay.com/checkin/user/20272978'

#定义一个递归函数遍历所有数据页面，返回数据list
def recur_link(url, header, cookie):
    #用于返回的数据list
    data = []
    #获取响应
    resp = requests.get(url, headers=header, cookies=cookie)
    #构造BeautifulSoup对象
    bsobj = BeautifulSoup(resp.text, 'html.parser')
    # 获取包含数据的容器
    ctan = bsobj.find('div', id='checkin')
    # 获得所有的文本
    texts = ctan.find_all('div', class_='note')
    for t in texts:
        text = t.string.strip()
        data.append(text)
    #获取下一页按钮
    btn = bsobj.find('a', class_="endless_page_link")
    if(btn != None):
        #构造正则表达式
        regex = re.compile(r'https://\w*\.\w*\.\w*')
        base_url = regex.match(url).group()
        url = ''.join((base_url, btn['href']))
        data.extend(recur_link(url, header, cookie))
    else:
        return data


#
# driver = webdriver.Chrome()
# driver.get(entry)
# bsobj = BeautifulSoup(driver.page_source, 'html.parser')
# div = bsobj.find('div', id='checkin')
# print("got!" if div != None else "don't get!")
# driver.close()
#获取header中的useragent
header = util.load_header('../header.txt')
#获取cookies
cookie = util.get_cookie_dic_from_file('cookie.txt')
#使用cookies请求url
data = recur_link(entry, header=header, cookie=cookie)
#保存提取的数据
util.save_obj(data, 'data.pkl')
