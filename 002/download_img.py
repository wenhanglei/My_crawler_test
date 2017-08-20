from requests import Request, Session
from bs4 import BeautifulSoup
import pickle

#指定需要爬取的url
url = 'http://www.putclub.com/'

#构造session对象
s = Session()
#设置整个会话的请求头
req_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Connection': 'keep-alive',
           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4'}
s.headers = req_header
#请求页面获得响应
resp = s.get(url)
#设置响应的编码格式
resp.encoding = resp.apparent_encoding
#构造Beautiful对象
bsobj = BeautifulSoup(resp.text, 'html.parser')
#查找所有img标签
imgs = bsobj.find_all('img')
#创建用于装载图片连接的list
img_links = []
#创建用于保存list的文件
file = open('imglinks.pkl', 'wb')
#打印所有图像标签的src属性
for img in imgs:
    if 'src' in img.attrs:
        img_links.append(img['src'])
#保存所有的图片连接
pickle.dump(img_links, file)


#打印获取的响应文本
# print(resp.text)


#获得response对象
# resp = requests.get(url)

# 打印获得的请求对象
# for (key, value) in s.headers.items():
#     print('%s: %s' % (key, value))

#设定response的编码为utf-8
# resp.encoding = 'utf-8'
#获得响应文本
# resp.text

#获得response对象的响应头
# headers = resp.headers

#打印响应头内容
# for (key, value) in headers.items():
#     print(key + ': ' + value)