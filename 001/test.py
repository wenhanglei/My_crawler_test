import requests
import base64
import io
import time

def download(id):
    return 'http://sited.ka94.com' + '/plugin.sited.php?id=' + str(id) + '&t=' + str(int(time.time()) + 180)

def get_url(text):
    data = base64.b64decode(bytes(text.split('?')[1],'utf-8'))
    url = data.decode('utf-8')
    return url

# r = requests.get(download(65))
# r.encoding = 'utf-8'
# with open('file.xml', 'w', encoding='utf-8') as file:
#     file.write(r.text)

def save_as_xml(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    with open('siteD.xml', 'w', encoding='utf-8') as file:
        file.write(resp.text)
