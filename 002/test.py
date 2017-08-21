from requests import Session
import requests
import request_header
from bs4 import BeautifulSoup
import pickle
import shutil
import os

# #获得图片连接
# file = open('sanbay.pkl', 'rb')
# links = pickle.load(file)
#
# def save_img(url, dirname = '.'):
#     "保存图片文件"
#     #获取文件名
#     filename = os.path.basename(url)
#     #生成文件路径
#     filepath = os.path.join(dirname, filename)
#     #拿到响应图片流
#     response = requests.get(url, stream=True)
#     #保存图片到指定文件夹
#     if not os.path.exists(filepath):
#         with open(filepath, 'wb') as f:
#             shutil.copyfileobj(response.raw, f)
#         del response
#
# #保存图片
# for link in links:
#     save_img(link)


# response = requests.get(url, stream=True)
# with open('img.png', 'wb') as out_file:
#     shutil.copyfileobj(response.raw, out_file)
# del response


#
# #指定需要爬取的url
# url = 'http://www.shanbay.com/web/account/login'
#
# #构造session对象
# s = Session()
# #设置整个会话的请求头
# s.headers = request_header.header
# #请求页面获得响应
# resp = s.get(url)
# #设置响应的编码格式
# resp.encoding = resp.apparent_encoding
# #构造Beautiful对象
# bsobj = BeautifulSoup(resp.text, 'html.parser')
# #查找所有img标签
# imgs = bsobj.find_all('img')
# #创建用于装载图片连接的list
# img_links = []
# #打开用于保存list的文件
# file = open("sanbay.pkl", 'wb')
# #打印所有图像标签的src属性
# for img in imgs:
#     if 'src' in img.attrs:
#         img_links.append(img['src'])
# #保存所有的图片连接
# pickle.dump(img_links, file)