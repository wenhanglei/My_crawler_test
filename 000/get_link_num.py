import requests
from bs4 import BeautifulSoup
import re
import sys

url = 'https://www.marxists.org/chinese/maozedong/index.htm#0'

def get_links_num(url):
    # 获取response对象
    response = requests.get(url)
    # 设置响应编码集
    response.encoding = response.apparent_encoding
    # 获得响应文本
    html = response.text
    # 构造beautifulsoup对象
    bsobj = BeautifulSoup(html, 'html.parser')
    # 返回所有的链接
    links = bsobj.find_all('a', href=re.compile('marxist*'))
    #返回当前页面内部连接数
    return len(links)

if __name__ == '__main__':
    link_num = get_links_num(url)
    print('this page has: %d links.' % link_num)

#
# #获得response对象
# response = requests.get(url)
# #设置响应编码集
# response.encoding = response.apparent_encoding
# #获得响应文本
# html = response.text
# #构造beautifulsoup对象
# bsobj = BeautifulSoup(html, 'html.parser')
# #返回所有的链接
# links = bsobj.find_all('a', href=re.compile('marxist*'))
#
#
#
# #获取response对象
# response = requests.get(url)
# #设置响应编码集
# response.encoding = response.apparent_encoding
# #获得响应文本
# html = response.text
# #构造beautifulsoup对象
# bsobj = BeautifulSoup(html, 'html.parser')
# #返回所有的链接
# links = bsobj.find_all('a', href=re.compile('marxist*'))
# #打印连接
# for link in links:
#     if 'href' in link.attrs:
#         print(link['href'])
#
# #获取响应头
# # headers = response.headers
# #打印响应头
# # for (header, value) in headers.items():
# #     print(header + ': ' + value)
#
# #获取response的二进制内容
# # b_text = response.content
# #对二进制内容使用GB2312进行解码
# # text = b_text.decode('GB2312')
# #打印解码后的文本
# # print(text)
#
# #对二进制进行解码
# # html = b_text.decode('gbk')
# # print(sys.getdefaultencoding())
# #获取response的文本
# # text = response.text.encode('ISO8859-1').decode('GBK')
# #得到response的当前编码集
# # print(response.apparent_encoding)
#
# #打印获得的网页文本
# # print(text)
