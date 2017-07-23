from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

def getLinks(urltail):
    url = 'https://www.marxists.org/chinese/maozedong/' + urltail
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    links = bs.find_all('a')
    return links


links = []
links = getLinks('index.htm#0')

while len(links) > 0:
    newarticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newarticle)
    links = getLinks(newarticle)
