#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from data import Data
from bs4 import BeautifulSoup
import pickle
import util

#是否打印记录的标志
flag = 1

#通过传递的BeautifulSoup对象获取并保存数据
def download_data(bsobj, container):
    div = bsobj.find('div', id='zh-list-collection-wrap')
    # 获取所有的class属性为zm-item的div
    sub_divs = div.find_all('div', class_='zm-item')
    # 遍历divs保存提取的数据
    for div in sub_divs:
        # 初始化数据容器
        data = Data()
        try:
            # 获取标题和连接
            data.title = div.h2.a.string
            data.link = 'https://www.zhihu.com' + div.h2.a['href']
            # 获取赞数和作者
            data.votes = div.find('div', class_='zm-item-vote').a.string
            data.author = div.find('span', class_='author-link-line').a.string
        except:
            print('something is wrong')
        # 保存数据
        if flag == 1:
            print('保存： ' + data.title)
            container.append(data)
            print('保存成功！')
        else:
            container.append(data)

def visite_next_link(url, contents):
    ##############获得页面内容，构造BeautifulSoup对象
    headers = util.load_header(header_file)
    r = requests.get(url, headers=headers)
    bsobj = BeautifulSoup(r.text, 'html.parser')
    #获取并保存需要提取的数据
    download_data(bsobj, contents)
    #获得包含下一页面的div
    foot_div = bsobj.find('div', class_='zm-invite-pager')
    #获得包含下一页的span
    next_page = foot_div.find_all('span')[-1]
    #如果该页面不是最后一页
    if next_page.a != None:
        #构造下一页的连接
        next_link = url.split('?')[0] + next_page.a['href']
        if flag == 1:
            print('访问：' + next_link)
            visite_next_link(next_link, contents)
        else:
            visite_next_link(next_link, contents)
    else:
        return None

if __name__ == '__main__':

    # 访问的入口网址
    url = 'https://www.zhihu.com/collection/30688692'
    # 用于加载的请求头文件
    header_file = 'header.txt'
    # 定义用于保存数据的list
    contents = []

    #访问并提取数据
    visite_next_link(url, contents)

    #保存数据
    with open('answer_links.pkl', 'wb') as file:
        pickle.dump(contents, file)








#############测试是否可以不用header和cookies直接访问
# r = requests.get(url)
# r.raise_for_status()
#*********测试后发现无法直接访问

#############测试修改user-agent之后是否能登录
#打印需要加载的请求头
# print(load_header(header_file))
#获得请求头dic
# headers = load_header(header_file)
#加载请求头后访问指定页面
# r = requests.get(url, headers = headers)
# r.raise_for_status()

#############################结论：需要修改ua才能访问一般以页面



# #拿到第一个sub_div获得数据
# sub_div = sub_divs[0]
#
# #获取标题和连接
# title = div.h2.a.string
# link = div.h2.a['href']
# #获取赞数和作者
# votes = div.find('div', class_='zm-item-vote').a.string
# author = div.find('span', class_='author-link-line').a.string

# #打印获得数据
# print('title:' + title)
# print('author:' + author)
# print('votes:' + votes)
# print('link:' + link)


