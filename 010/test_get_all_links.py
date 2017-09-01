#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from util import *
from bs4 import BeautifulSoup
import csv

#需要爬取连接的导航网站的入口
url = 'http://ilxdh.com'
headers = load_header('header.txt')

#爬取网页获得响应
resp = requests.get(url, headers=headers)
bsobj = BeautifulSoup(resp.text, 'html.parser')
#获得所有的连接对象
links = bsobj.find_all('a')
#构造csvwriter
with open('links.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    for link in links:
        if 'href' in link.attrs:
            link_href = link['href']
            if link_href.startswith('http:'):
                if link.string:
                    name = link.string.strip()
                    writer.writerow((name, link_href))