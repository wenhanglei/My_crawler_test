import requests

url = "http://www.toutiao.com/c/user/4488814447/"
cookie_file = 'cookie.txt'
header_file = 'request_headers.txt'

#从txt文件加载cooki字典
def get_cookie_dic(filename):
    cookies = {}
    with open(filename) as file:
        cookie_text = file.read()
        ck_li = cookie_text.split(';')
        for li in ck_li:
            key, value = tuple(li.split('=', maxsplit=1))
            cookies[key] = value
    return cookies
#从txt文件加载header字典
def load_header_dic(filename):
    headers = {}
    with open(filename) as file:
        for line in file:
            key, value = line.rstrip().split(':', maxsplit=1)
            headers[key] = value
    return headers

if __name__ == '__main__':
    #测试加载的cookie和header
    # for key, value in get_cookie_dic(cookie_file).items():
    #     print('%s : %s' % (key, value))
    #测试加载的header
    # for key, value in load_header_dic(header_file).items():
    #     print('%s : %s' % (key, value))
    #加载header
    headers = load_header_dic(header_file)
    # #加载cookies
    cookie = get_cookie_dic(cookie_file)
    # 请求登录后网页
    with requests.Session() as s:
        s.headers = headers
        resp = s.get(url, cookies=cookie)
        #设置响应编码
        resp.encoding = resp.apparent_encoding
        with open('page.html', 'w', encoding='utf-8') as file:
            file.write(resp.text)

