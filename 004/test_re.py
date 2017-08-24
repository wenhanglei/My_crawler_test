import re

string = open('text.html').read()
p = re.compile(r'<img.*?>')
m = p.search(string)
print(m.group())