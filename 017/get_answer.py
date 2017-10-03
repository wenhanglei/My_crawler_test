#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import util

# html = """<noscript><img class="origin_image zh-lightbox-thumb" data-original="https://pic1.zhimg.com/v2-8fc79e5977ccce43a89bcfc7cfe99ed4_r.jpg" data-rawheight="2448" data-rawwidth="3264" src="https://pic1.zhimg.com/50/v2-8fc79e5977ccce43a89bcfc7cfe99ed4_hd.jpg" width="3264"/></noscript><img class="origin_image zh-lightbox-thumb lazy" data-actualsrc="https://pic1.zhimg.com/50/v2-8fc79e5977ccce43a89bcfc7cfe99ed4_hd.jpg" data-original="https://pic1.zhimg.com/v2-8fc79e5977ccce43a89bcfc7cfe99ed4_r.jpg" data-rawheight="2448" data-rawwidth="3264" src="data:image/svg+xml;utf8,&lt;svg%20xmlns='http://www.w3.org/2000/svg'%20width='3264'%20height='2448'&gt;&lt;/svg&gt;" width="3264">"""

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
    for a in list(i.attrs):
        del i[a]

print(bsobj.prettify())



# del bsobj.noscript.img['class']
# del bsobj.noscript.img['data-original']
#
# img = bsobj.noscript.img.extract()
# bsobj.noscript.replace_with(img)


# print(bsobj.prettify())
