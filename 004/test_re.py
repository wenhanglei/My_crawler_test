import requests
import pickle

#保存cookies
def save_cookies(s):
    with open('cookies', 'wb') as file:
        pickle.dump(s.cookies, file)

#加载cookies
def load_cookies():
    with open('cookies', 'rb') as file:
        cookies = pickle.load(file)
        return cookies

#通过header.txt载入用于设置request的header
def load_header(filename):
    header = {}
    with open(filename) as file:
        for line in file:
            key,value = line.rstrip().split(':', maxsplit=1)
            header[key] = value
    return header



# url = 'https://sso.toutiao.com/login/'
# header_file = 'header.txt'
# # 创建会话对象
# with requests.Session() as s:
#     # 装载请求头
#     s.headers = load_header(header_file)
#     # 访问登录页面，返回响应
#     resp = s.get(url)
#     # 设置resp的编码格式为utf8
#     resp.encoding = 'utf-8'
#     #保存cookies
#     save_cookies(s)