import requests
from bs4 import BeautifulSoup
import pickle

# #定义用于保存数据的结构
# data = []

#通过观察发现所有需要爬取的页面都有类似的结构
#https://movie.douban.com/top250?start=0&filter=
#https://movie.douban.com/top250?start=25&filter=

#https://movie.douban.com/top250?start=225&filter=


#指定URL，传入用于装载数据的data，即可返回得到的数据
def load_data(url, data):
    r = requests.get(url)
    #构建BeautifulSoup对象
    bsobj = BeautifulSoup(r.text, 'html.parser')
    #返回包含所有图片的主体标签
    ol = bsobj.find('ol', class_='grid_view')
    #返回包含图片连接的div
    divs = ol.find_all('div', class_='pic')
    #遍历取得div标签
    for div in divs:
        #创建用于封装数据的dict
        item = {}
        #获得图片的连接
        item['href'] = div.a['href']
        #获得图片的名称
        item['title'] = div.a.img['alt']
        #获得缩略图src
        item['img_src'] = div.a.img['src']
        #保存item到data中
        data.append(item)

if __name__ == '__main__':
    #定义用于保存数据的list
    data = []

    # 遍历需要爬取的页面
    for i in range(10):
        url = 'https://movie.douban.com/top250?start=%s&filter=' % str(i * 25)
        #获取数据
        load_data(url, data)

    #保存爬取的data数据
    with open('img_data.pkl', 'wb') as file:
        pickle.dump(data, file)