#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util
import requests

#下载知乎文章的函数
def download_article():
    pass


#下载普通答案的函数
def download_answer():
    pass


#函数调用区（用于测试和实际运行）
if __name__ == '__main__':
    #外部函数调用需要提供：文章地址article_addr, 用于加载的useragent
    article_addr = 'https://zhuanlan.zhihu.com/p/30546947'
    header = util.load_header('../header.txt')
    #访问目标网站，保存获得的html
    resp = requests.get(article_addr, headers=header)
    util.save_html('download.html', resp.text)
