import requests
import re
# from bs4 import BeautifulSoup

#通过header.txt载入用于设置request的header
def load_header(filename):
    header = {}
    with open(filename) as file:
        for line in file:
            key,value = line.rstrip().split(':', maxsplit=1)
            header[key] = value
    return header



if __name__ == '__main__':

    header_file = 'header.txt'
    url = 'https://sso.toutiao.com/login/'

    #####获取验证码
    #创建会话对象
    with requests.Session() as s:
        #装载请求头
        s.headers = load_header(header_file)
        #访问登录页面，返回响应
        resp = s.get(url)
        #设置resp的编码格式为utf8
        resp.encoding = 'utf-8'
        #创建用于匹配图片的正则表达式
        pattern = re.compile(r'<img.*?>')
        img_list = pattern.findall(resp.text)
        if img_list != []:
            for img in img_list:
                print(img)
        else:
            print('没有获取到！')
        # #构建BeautifulSoup对象
        # bsobj = BeautifulSoup(resp.text, 'html.parser')
        # #取得表单对象
        # form = bsobj.find('form')
        # #打印表单对象
        # print(form.prettify())
        # #取得验证码对象
        # captcha = bsobj.find('img', class_='y-right captcha')
        # #打印captcha的src属性
        # if  captcha != None:
        #     print(captcha['src'])
        # else:
        #     print('获取失败！')


# ###################################################################
#     #创建会话对象
#     with requests.Session() as s:
#         #装载请求头
#         s.headers = load_header(header_file)
#         #访问登录页面，返回响应
#         resp = s.get(url)
#         #打印响应状态码
#         print(resp.status_code)
#         print('#' * 100)
#         #打印此时的cookies
#         for key, value in s.cookies.items():
#             print('%s = %s' % (key, value))
# #####################################################################