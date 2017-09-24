#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

#控制台打印进度条
def print_progress(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    """
    call in a loop to create a progressbar:
    :param iteration:  current iteration(int)
    :param total:      total iteration(int)
    :param prefix:     prefix string(str)
    :param suffix:      suffix string(str)
    :param decimals:   positive number precision
    :param length:     character length for bar
    :param fill:       bar fill character
    :return: 
    """
    percent = ("{0:." + str(decimals) + "f}").format(100*(iteration/float(total)))
    fill_length = int(length*iteration//total)
    bar = fill*fill_length + '-'*(length-fill_length)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='')


#将扇贝的时间格式转化成mysql的时间格式
def convert_timeformat(date):
    regex = re.compile(r'(\w*)月 (\d*), (\d*)')
    m = regex.match(date)
    month = convert_num(m.group(1))
    day = m.group(2)
    year = m.group(3)
    return ('%s-%s-%s' % (year, str(month), day))

#中文数字转化为罗马数字
def convert_num(c):
    arr = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二']
    if c in arr:
        return arr.index(c)+1

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

#从txt文件加载cookie字典
def get_cookie_dic_from_file(filename):
    "return dic"
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