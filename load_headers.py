header_file = 'request_headers.txt'

def load_header_dic(filename):
    headers = {}
    with open(filename) as file:
        for line in file:
            key, value = line.rstrip().split(':', maxsplit=1)
            headers[key] = value
    return headers


if __name__ == '__main__':
    #测试加载的heade
    for key, value in load_header_dic(header_file).items():
        print('%s : %s' % (key, value))
    # load_header_dic(header_file)
