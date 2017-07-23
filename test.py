from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import datetime

random.seed(datetime.datetime.now())

def getLinks(urltail):
    url = 'https://www.marxists.org/chinese/maozedong/' + urltail
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find_all('a')

links = getLinks('index.htm#0')
print('haha')