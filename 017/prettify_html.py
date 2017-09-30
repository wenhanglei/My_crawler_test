#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

infi =  'download.html'
with open(infi, 'r') as f:
    bsobj = BeautifulSoup(f.read())
    print(bsobj.prettify())