#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import util
import re
import shutil
import os
import requests

infi =  'download.html'
with open(infi, 'r') as f:
    bsobj = BeautifulSoup(f.read(), 'html.parser')
    del bsobj.span['class']
    del bsobj.span['itemprop']

ncts = bsobj.find_all('noscript')

for n in ncts:
    n.decompose()

imgs = bsobj.find_all('img')

for i in imgs:
    #如果img包含src属性
    if 'data-actualsrc' in i.attrs:
        img_url = i['data-actualsrc']
        for a in list(i.attrs):
            del i[a]
        i['src'] = util.get_img(img_url, 'images')



#保存新生成的html
util.save_html('test.html', str(bsobj))



