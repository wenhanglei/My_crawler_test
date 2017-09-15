#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import util
from bs4 import BeautifulSoup
import requests

#访问入口
entry = 'https://www.shanbay.com/checkin/user/20272978'
#
# driver = webdriver.Chrome()
# driver.get(entry)
# bsobj = BeautifulSoup(driver.page_source, 'html.parser')
# div = bsobj.find('div', id='checkin')
# print("got!" if div != None else "don't get!")
# driver.close()
#获取header中的useragent
header = util.load_header('../header.txt')
#获取cookies
cookie = util.get_cookie_dic_from_file('cookie.txt')
#使用cookies请求url
resp = requests.get(entry, headers=header, cookies=cookie)
#保存获得响应文件
util.save_obj(resp.text, 'html')
