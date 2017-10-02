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

for c in bsobj.descendants:
    if c.name == 'noscript':
        print(c)




