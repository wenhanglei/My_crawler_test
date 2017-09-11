#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import util

#设定爬取的网站入口
url = "https://www.economist.com"

#测试是否可以直接爬取
resp = requests.get(url)
#构造beautifulsoup对象
bsobj = BeautifulSoup(resp.text, 'html.parser')
link = bsobj.find('a', class_='latest-updates-panel-card')
if 'href' in link.attrs:
    resp = requests.get(url + link['href'])
    bsobj = BeautifulSoup(resp.text, 'html.parser')
    text_div = bsobj.find('div', class_='blog-post__text')
    util.save_obj(text_div.prettify(), 'text_div')