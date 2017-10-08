#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

#访问的入口网址
entry_url = 'http://www.weather.com.cn/data/sk/101042800.html'
r = requests.get(entry_url)
r.encoding = 'utf-8'
print(r.json())


