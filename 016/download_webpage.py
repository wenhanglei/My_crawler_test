#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import itertools
from urllib.error import URLError
from urllib.request import urlopen
from urllib.request import Request

def link_crawler(seed_url, link_regex):
    """从给定的url爬取匹配正则表达式的所有连接"""
    crawl_queue = [seed_url]
    #记录访问过的url
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        #过滤匹配正则表达式的连接
        for link in get_links(html):
            if re.match(link_regex, link):
                link = urlparse.urljoin(seed_url, link)
                if link not in seen:
                    seen.append(link)
                    crawl_queue.append(link)

def get_link(html):
    """返回连接list"""
    #提取所有链接的正则表达式
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)

#下载指定url的网页
def download(url, user_agent='cute_spider', num_retries=2):
    print('Downloading:', url)
    headers = {'User-agent:': user_agent}
    request = Request(url, headers=headers)
    try:
        html = urlopen(request).read()
    except URLError as e:
        print('Download error: ', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent, num_retries-1)
    return html

#获得sitemap所有的链接
def crawl_sitemap(url):
    #下载sitemap文件
    sitemap = download(url)
    #提取sitemap中的所有链接
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    #遍历所有链接
    for link in links:
        html = download(link)

if __name__ == '__main__':
    sitemap = download('https://example.webscraping.com/sitemap.xml')
    links = re.findall(b'<loc>(.*?)</loc>', sitemap)
    for i in range(3):
        print(links[i])