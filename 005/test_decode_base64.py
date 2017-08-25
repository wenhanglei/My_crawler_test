filename = 'image'
import re
import base64

with open(filename) as file:
    text = file.read()
    p = re.compile(r'data:image/gif;base64,(.*)')
    m = p.search(text)
    print(m.group(1))
    data = bytes(m.group(1),'utf-8')
    img = base64.b64decode(data)
    with open('captcha.gif', 'wb') as ofile:
        ofile.write(img)