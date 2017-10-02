#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

html = '<noscript><img class="origin_image zh-lightbox-thumb" data-original="https://pic1.zhimg.com/v2-8fc79e5977ccce43a89bcfc7cfe99ed4_r.jpg" data-rawheight="2448" data-rawwidth="3264" src="https://pic1.zhimg.com/50/v2-8fc79e5977ccce43a89bcfc7cfe99ed4_hd.jpg" width="3264"/></noscript>'

bsobj = BeautifulSoup(html, 'html.parser')

del bsobj.noscript.img['class']
del bsobj.noscript.img['data-original']


print(bsobj.prettify())
