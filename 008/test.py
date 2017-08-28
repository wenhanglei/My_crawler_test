#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os
import time

url = 'http://sited.ka94.com'

# r = requests.get(url)
# bsobj = BeautifulSoup(r.text, 'html.parser')
# scripts = bsobj.find_all('script')
# for s in scripts:
#     if 'src' in s.attrs:
#         link = s['src']
#         if link.startswith('/js'):
#             n_link = url + link
#             filename = os.path.basename(n_link)
#             resp = requests.get(n_link)
#             resp.encoding = 'utf-8'
#             with open(filename, 'w') as file:
#                 file.write(resp.text)

# function download(el, id) {
#
#     window.location = "sited://data?" + BASE64.encoder(window.location.origin + "/plugin.sited.php?id=" + id + "&t=" + (Math.round(new Date().getTime() / 1000) + 180));
#
# }

def download(id):
    return 'http://sited.ka94.com' + '/plugin.sited.php?id=' + str(id) + '&t=' + str(int(time.time()) + 180)

print(download(65))