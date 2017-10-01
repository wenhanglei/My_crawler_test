#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import util
import requests
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/question/61046076/answer/185135407'
header = util.load_header('../header.txt')
resp = requests.get(url, headers = header)

bsobj = BeautifulSoup(resp.text, 'html.parser')
div = bsobj.find('span', class_='RichText')

with open('download.html', 'w') as f:
    f.write(str(div))

