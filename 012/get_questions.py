#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

#请求url
req_url = 'https://www.zhihu.com/people/yu-tian-50-3/following/questions'

def get_questions(result):
    try:
        #获取下一页按钮
        btn = driver.find_element_by_class_name('PaginationButton-next')
    except NoSuchElementException as exception:
        # 构造bsobj
        bsobj = BeautifulSoup(driver.page_source, 'html.parser')
        # 获取包含item的容器
        div = bsobj.find('div', id="Profile-following")
        ques_div = div.find_all('div', class_="QuestionItem-title")
        for ques in ques_div:
            result.append(ques.string)
        return result
    else:
        # 构造bsobj
        bsobj = BeautifulSoup(driver.page_source, 'html.parser')
        div = bsobj.find('div', id='Profile-following')
        ques_div = div.find_all('div', class_="QuestionItem-title")
        for ques in ques_div:
            result.append(ques.string)
        #跳转到下一页
        btn.send_keys(Keys.RETURN)
        return get_questions(result)

def get_ques(result, wait):
    try:
        btn = driver.find_element_by_class_name('PaginationButton-next')
    except NoSuchElementException:
        divs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'QuestionItem-title')))
        for div in divs:
            result.append(div.find_element_by_tag_name('a').text)
        return result
    else:
        divs = wait.until(load_all_elements('QuestionItem-title'))
        for div in divs:
            result.append(div.find_element_by_tag_name('a').text)
        btn.send_keys(Keys.RETURN)
        return get_ques(result, wait)

#自定义一个检查网页是否加载完全的wait条件
class load_all_elements(object):
    def __init__(self, locater):
        self.locater = locater
    def __call__(self, driver):
        elements = driver.find_elements_by_class_name(self.locater)
        if len(elements) == 20:
            return elements
        else:
            return false


#加载cookies
# cookies = util.get_cookie_dic_from_file('cookie.txt')
# for key,value in cookies.items():
#     print("%s : %s" % (key,value))
#加载headers
# header = util.load_header('../header.txt')
#
# #不使用session直接通过get获得响应
# resp = requests.get(req_url, headers=header)
# #构造BeautifulSoup
# bsobj = BeautifulSoup(resp.text, 'html.parser')
# #获取包含item的容器
# div = bsobj.find('div', id="Profile-following")
# ques_div = div.find_all('div', class_="List-item")
# print(bsobj.prettify())
# print(len(ques_div))

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

# driver = webdriver.Chrome()
# driver.get(req_url)
# #获取结果集
# result = []
# get_questions(result)
# #保存获取的结果
# util.save_obj(result, 'questions.pkl')
# driver.close()

driver = webdriver.Chrome()
driver.get(req_url)
result = []
wait = WebDriverWait(driver, 10)
get_ques(result, wait)
print(len(result))
util.save_obj(result, 'questions.pkl')
time.sleep(1)
driver.close()