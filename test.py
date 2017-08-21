import requests

#def download(url):
#    return requests.get(url).content
#
# ###################################################
# def download(url):
#     print('downloading: ' + url)
#     try:
#         html = requests.get(url).content
#     except requests.HTTPError as e:
#         print('something is wrong!')
#         html = None
#     return html
###################################################
# def download(url, num_retrieve=2):
#     print('downloading: ' + url)
#     try:
#         html = requests.get(url).content
#     except requests.HTTPError as e:
#         print('something is wrong!')
#         html = None
#         if num_retrieve > 0:
#             code = e.respoonse.status_code
#             if code != None and 500 <= code < 600:
#                 return download(url, num_retrieve-1)
#     return html
#
# url = 'http://www.ilxdh.com'
# html = download(url)
# with open('text.html', 'wb') as file:
#     file.write(html)
