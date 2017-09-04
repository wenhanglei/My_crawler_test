#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

#通过list获得cookies的dic
def get_cookie_dic_from_co_li(co_li):
    # 用于装载常规cookie的dir
    cookies = {}
    for cookie in filename:
        cookies[cookie['name']] = cookie['value']
    return cookies

#通过header.txt载入用于设置request的header
def load_header(filename):
    header = {}
    with open(filename) as file:
        for line in file:
            key,value = line.rstrip().split(':', maxsplit=1)
            header[key] = value
    return header

#从txt文件加载cooki字典
def get_cookie_dic_from_file(filename):
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