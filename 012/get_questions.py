#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

#请求url
req_url = 'https://www.zhihu.com/people/yu-tian-50-3/following/questions'

#加载cookies
cookies = util.get_cookie_dic_from_file('cookie.txt')
# for key,value in cookies.items():
#     print("%s : %s" % (key,value))
#加载headers
header = util.load_header('../header.txt')
#创建session访问
# with requests.session() as s:
#     s.headers = header
#     #获取响应
#     rep = s.get(req_url, cookies=cookies)
#     #设置响应编码
#     rep.encoding = 'utf-8'
#     #构造bsobj
#     bsobj = BeautifulSoup(rep.text, 'html.parser')
#     #获取包含item的容器
#     div = bsobj.find('div', id="Profile-following")
#     ques_div = div.find_all('div', class_="List-item")
#     print(bsobj.prettify())
#     print(len(ques_div))
#     # for que in ques_div:
#     #     print(que.string)

driver = webdriver.Chrome()
driver.get(req_url)
#构造bsobj
bsobj = BeautifulSoup(driver.page_source, 'html.parser')
#获取包含item的容器
div = bsobj.find('div', id="Profile-following")
ques_div = div.find_all('div', class_="List-item")
print(bsobj.prettify())
print(len(ques_div))
driver.close()


