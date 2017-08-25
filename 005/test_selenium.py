from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://sso.toutiao.com/login/")
form = driver.find_element(By.TAG_NAME, 'form')
html = form.get_attribute('outerHTML')
bsobj = BeautifulSoup(html, 'html.parser')
captcha = bsobj.find('img')
with open('image','w') as file:
    file.write(captcha['src'])
driver.close()