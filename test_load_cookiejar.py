import http.cookiejar

#加载保存的cookiejar
filename = 'cookies'
cj = http.cookiejar.MozillaCookieJar(filename)
#加载cookies文件
cj.load()
cj.revert('cookies1')
#遍历打印cookie的内容
for cookie in cj:
    print(cookie.name + ': ' + cookie.value)