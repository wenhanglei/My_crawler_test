#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#登录页面
login_url = "https://accounts.douban.com/"


driver = webdriver.Chrome()
driver.get(login_url)
email = driver.find_element_by_id('email')
#输入的帐号
email.clear()
email.send_keys('3188****.com')
#获取密码输入框
password = driver.find_element_by_id('password')
password.clear()
#输入密码
password.send_keys('******')
#获得登录按钮
submit = driver.find_element_by_class_name('btn-submit')
#点击登录按钮
submit.send_keys(Keys.RETURN)
#等待两秒
time.sleep(2)
#获取cookies对象
cookies = driver.get_cookies()
#保存获取的cookies对象
util.save_obj(cookies, 'cookies.pkl')
#关闭打开的driver
driver.close()
