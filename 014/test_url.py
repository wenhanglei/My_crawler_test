#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

entry = 'https://www.shanbay.com/checkin/user/20272978'
file = r'e:\pycharm_demo\my_crawler_text\test.py'
relurl = '/checkin/user/20272978/?page=85'

# pattern = re.compile(r'https://\w*\.\w*\.\w*')
# match = pattern.match(entry)
# base_url = match.group()
# print(base_url)
# print(''.join((base_url, relurl)))

arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7]

arr1.extend(arr2)
print(arr1)