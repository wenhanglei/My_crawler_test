from bs4 import BeautifulSoup

html = '<span>hello world</span>'

bo = BeautifulSoup(html, 'html.parser')

print(bo.find('span').a)