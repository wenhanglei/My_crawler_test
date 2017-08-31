#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.parse
import requests
from bs4 import BeautifulSoup


#指定城市获取用于访问的入口url
def get_url(city):
    urlcode = urllib.parse.quote(city, encoding='utf-8')
    return 'https://www.lagou.com/jobs/list_Python?px=default&city=%s' % urlcode



#通过header.txt载入用于设置request的header
def load_header(filename):
    header = {}
    with open(filename) as file:
        for line in file:
            key,value = line.rstrip().split(':', maxsplit=1)
            header[key] = value
    return header

#从txt文件加载cooki字典
def get_cookie_dic(filename):
    cookies = {}
    with open(filename) as file:
        cookie_text = file.read()
        ck_li = cookie_text.split(';')
        for li in ck_li:
            key, value = tuple(li.split('=', maxsplit=1))
            cookies[key] = value
    return cookies

#保存对象到指定文件
def save_obj(obj, fname):
    import pickle
    with open(fname, 'wb') as file:
        pickle.dump(obj, file)

#从指定文件读取数据
def load_obj(fname):
    import pickle
    with open(fname, 'rb') as file:
        return pickle.load(file)

# cookies = get_cookie_dic('cookies.txt')
# headers = load_header('header.txt')
# url = get_url('重庆')
# resp = requests.get(url, headers=headers, cookies=cookies)
# resp.encoding = 'utf-8'
# resp.raise_for_status()
# save_obj(resp.text, 'html.pkl')

html = load_obj('html.pkl')
bsobj = BeautifulSoup(html, 'html.parser')
item_con = bsobj.find_all('ul', class_='item-con-list')
print(len(item_con))