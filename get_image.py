from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = r'https://www.marxists.org/chinese/maozedong/index.htm#0'
html = urlopen(url)
bobj = BeautifulSoup(html.read(),"html.parser")

imgurl = bobj.find('img')['src']
absurl = urljoin(url, imgurl)
urlretrieve(absurl, 'mao.jpg')