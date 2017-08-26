import pickle
import shutil
import requests
import os

#创建用于保存图片文件的文件夹
dirname = 'top250_images'
if not os.path.exists(dirname):
    os.mkdir(dirname)
with open('img_data.pkl', 'rb') as file:
    data = pickle.load(file)
    for item in data:
        #构建图片名
        img_name = item['title'] + '.jpg'
        #获得用于保存的文件路径
        imgpath = os.path.join(dirname, img_name)
        #获得图片下载的url
        img_url = item['img_src']
        #下载保存图片文件
        with open(imgpath, 'wb') as imgfile:
            r = requests.get(img_url, stream=True)
            shutil.copyfileobj(r.raw, imgfile)
            del r