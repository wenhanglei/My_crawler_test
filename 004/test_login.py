import requests
import re
import base64
from PIL import Image
import io
import pickle
# from bs4 import BeautifulSoup

#保存cookies
def save_cookies(s):
    with open('cookies', 'wb') as file:
        pickle.dump(s.cookies, file)

#加载cookies
def load_cookies(s):
    with open('cookies', 'rb') as file:
        cookies = pickle.load(file)
        s.cookies = cookies

#匹配str对象获得base64编码的验证码
def get_raw_captcha(html):
    p = re.compile(r"captcha: '(.*?)'")
    m = p.search(html)
    return m.group(1)

#直接通过验证码的base64编码显示图像
def show_captcha(captcha):
    # 把str对象转变成bytes对象用于base64解码
    data = bytes(captcha, 'utf-8')
    # 解码获得图像数据
    img = base64.b64decode(data)
    # 显示图像
    Image.open(io.BytesIO(img)).show()


#对str对象解码生成验证码并保存(不需要使用）
def save_captcha(src_string):
    #把str对象转变成bytes对象用于base64解码
    data = bytes(src_string, 'utf-8')
    #解码获得图像数据
    img = base64.b64decode(data)
    #保存验证码到captcha.gif
    with open('captcha.gif', 'wb') as ofile:
        ofile.write(img)

#通过header.txt载入用于设置request的header
def load_header(filename):
    header = {}
    with open(filename) as file:
        for line in file:
            key,value = line.rstrip().split(':', maxsplit=1)
            header[key] = value
    return header



if __name__ == '__main__':

    url = 'https://sso.toutiao.com/login/'
    action_url = 'https://sso.toutiao.com/login/auth/login'
    header_file = 'header.txt'
    #创建会话对象
    with requests.Session() as s:
        #装载请求头
        s.headers = load_header(header_file)
        #访问登录页面，返回响应
        resp = s.get(url)
        #设置resp的编码格式为utf8
        resp.encoding = 'utf-8'
        #post的表单内容
        data = {'account': '',
                'password': ''}
        #显示验证码
        captcha = get_raw_captcha(resp.text)
        show_captcha(captcha)
        data['captcha'] = input().rstrip()
        #进行登录操作
        r = s.post(action_url, data=data)
        #保存登录后的cookies
        save_cookies(s)
        #返回响应状态码
        r.raise_for_status()


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