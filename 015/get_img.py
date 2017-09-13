#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os
import shutil

def get_img(url):
    baseurl = 'https://login.kongfz.com'
    basename = os.path.basename(url)
    r = requests.get(baseurl+url, stream=True)
    with open(basename, 'wb') as img:
        shutil.copyfileobj(r.raw, img)


url = '/pc/images/login/logo.png'
get_img(url)