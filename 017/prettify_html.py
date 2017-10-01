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
    imgs = bsobj.find_all('img',src=re.compile(r'^https*'))
    for i in imgs:
        if 'src' in i.attrs:
            dir_path = 'img'
            util.get_img(i['src'], dir_path)
            basename = os.path.basename(i['src'])
            i['src'] = os.path.join(dir_path, basename)
    print(bsobj.prettify())


