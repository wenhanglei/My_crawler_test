import request_header
import os
import shutil
import requests
from requests import Session
from bs4 import BeautifulSoup

#通过url获取网页中所有图片src连接保存到指定文件
# def dump_img_links(url, filename):
#     #构造session对象
#     s = Session()
#     #设置整个会话的请求头
#     s.headers = request_header.header
#     #请求页面获得响应
#     resp = s.get(url)
#     #设置响应的编码格式
#     resp.encoding = resp.apparent_encoding
#     #构造Beautiful对象
#     bsobj = BeautifulSoup(resp.text, 'html.parser')
#     #查找所有img标签
#     imgs = bsobj.find_all('img')
#     #创建用于装载图片连接的list
#     img_links = []
#     #打开用于保存list的文件
#     file = open(filename, 'wb')
#     #打印所有图像标签的src属性
#     for img in imgs:
#         if 'src' in img.attrs:
#             img_links.append(img['src'])
#     #保存所有的图片连接
#     pickle.dump(img_links, file)

def get_link_list(url):
    # 构造session对象
    s = Session()
    # 设置整个会话的请求头
    s.headers = request_header.header
    try:
        # 请求页面获得响应
        resp = s.get(url)
        # 设置响应的编码格式
        resp.encoding = resp.apparent_encoding
        # 构造Beautiful对象
        bsobj = BeautifulSoup(resp.text, 'html.parser')
    except:
        print('无法连接： ' + sys.exc_info()[1])
        5/0
    else:
        # 查找所有img标签
        imgs = bsobj.find_all('img')
        # 创建用于装载图片连接的list
        img_links = []
        # 保存所有图片的原始连接
        for img in imgs:
            if 'src' in img.attrs:
                img_links.append(img['src'])
        return img_links

def save_img(url, dirpath = '.'):
    "保存图片文件"
    #获取文件名
    filename = os.path.basename(url)
    #生成文件路径
    filepath = os.path.join(dirpath, filename)
    try:
        #拿到响应图片流
        response = requests.get(url, stream=True)
    except:
        print('提供的连接不对!')
        1/0
    else:
        #保存图片到指定文件夹
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as f:
                shutil.copyfileobj(response.raw, f)
            del response

def download_imgs(url, dirpath = '.'):
    #获得可以访问的连接list
    links = get_link_list(url)
    #遍历list保存图片
    for link in links:
        save_img(link, dirpath)


if __name__ == '__main__':
    # 指定需要爬取的url
    url = 'http://www.shanbay.com/web/account/login'
    #下载所有图片
    download_imgs(url)