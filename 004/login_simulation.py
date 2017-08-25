"""
模拟登录今日头条网页
"""
import requests
from bs4 import BeautifulSoup
import re

url = 'https://sso.toutiao.com/login/'

resp = requests.get(url)
print(resp.text)