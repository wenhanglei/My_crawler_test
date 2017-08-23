import http.cookiejar
import urllib.request
import request_header

url = 'https://en.wikipedia.org/wiki/Main_Page'

#创建用于装载cookie的cookiejar
cj = http.cookiejar.MozillaCookieJar()
#初始化绑定cookiejar的请求
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#访问url
opener.open(url)
#保存返回的cookie对象
filename = 'cookies1'
cj.save(filename)


