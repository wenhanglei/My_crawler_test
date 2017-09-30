#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import util
import requests
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/question/56838287/answer/152755557'
header = util.load_header('../header.txt')
resp = requests.get(url, headers = header)

bsobj = BeautifulSoup(resp.text, 'html.parser')
div = bsobj.find('div', class_='RichContent')

with open('download.html', 'w') as f:
    f.write(str(div))

