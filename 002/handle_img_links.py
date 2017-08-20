import pickle

#访问的website
# url = 'http://www.putclub.com'
# pkl_file = 'imglinks.pkl'

def handle_img_links(url, pkl_file):
    #获取存储的图片连接
    img_links = pickle.load(open(pkl_file, 'rb'))

    #创建新的list用于装载处理后的图片连接
    filled_links = []
    #对连接进行筛选和补全
    for i in img_links[1:]:       #排除第一个php页面
        #如果不为空
        if i != '':
            #剔除所有的url头
            i = i.replace(url, '')
            #补全所有的连接
            i = url + i
            #添加补全后的连接
            filled_links.append(i)
    return filled_links
