#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util
from bs4 import BeautifulSoup

text_div = util.load_obj('text_div')
# print(text_div)
#构造beautifulsoup对象
bsobj = BeautifulSoup(text_div, 'html.parser')
ps = bsobj.find_all('p')
string = ''
for p in ps:
    string += p.get_text().strip()
for s in string.split('.'):
    print(s)
