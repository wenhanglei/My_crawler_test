#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import util
from bs4 import BeautifulSoup

#访问入口
entry = 'https://www.shanbay.com/checkin/user/20292978'
#
# driver = webdriver.Chrome()
# driver.get(entry)
# bsobj = BeautifulSoup(driver.page_source, 'html.parser')
# div = bsobj.find('div', id='checkin')
# print("got!" if div != None else "don't get!")
# driver.close()

