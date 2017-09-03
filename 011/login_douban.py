#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util
from selenium import webdriver

#登录页面
login_url = "https://accounts.douban.com/"


driver = webdriver.Chrome()
driver.get(login_url)
print(driver.page_source)