#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

#设定爬取的网站入口
url = "https://www.economist.com"

#测试是否可以直接爬取
resp = requests.get(url)
