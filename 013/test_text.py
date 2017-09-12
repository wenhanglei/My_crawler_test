#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util
from bs4 import BeautifulSoup

text_div = util.load_obj('text_div')
# print(text_div)
#构造beautifulsoup对象
bsobj = BeautifulSoup(text_div, 'html.parser')
print(bsobj.get_text())
