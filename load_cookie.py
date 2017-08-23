file = 'cookie.txt'

def get_cookie_dic(filename):
    cookies = {}
    with open(filename) as file:
        cookie_text = file.read()
        ck_li = cookie_text.split(';')
        for li in ck_li:
            key, value = tuple(li.split('=', maxsplit=1))
            cookies[key] = value
    return cookies

for key, value in get_cookie_dic(file).items():
    print('%s = %s' % (key, value))