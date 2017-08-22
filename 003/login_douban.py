# cookies = 'll="108309"; bid=6xdC2d2XN9I; gr_user_id=1cd088c8-2b69-416b-8064-7a5d71ffd334; UM_distinctid=15d8c583862613-04a2e2ffb8da45-333f5902-100200-15d8c58386c28de; viewed="26740503_25814739_26274202_26869212_26999123_26869992_3082278_21792530_1231579_2228378"; _vwo_uuid_v2=9DDAA51B1AA3BA46F3B461EA4110B63D|a592eab55e5c3ca5f5b9608200c1ff64; ps=y; push_noty_num=0; push_doumail_num=0; ap=1; __utma=30149280.729731874.1498746693.1503371976.1503386476.9; __utmc=30149280; __utmz=30149280.1503386476.9.7.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; __utmv=30149280.13248; _ga=GA1.2.729731874.1498746693; _gid=GA1.2.1142111036.1503371979; ue="3188744608@qq.com"; dbcl2="132482335:GLv31nzKCf0"; ck=o-5E'
def change_cookies(cookiestr):
    li = cookiestr.split(';')
    cookies = {}
    for i in li:
        item = i.split("=")
        if item[1].startswith('"'):
            cookies[item[0]] = item[1][1:-2]
            # print('%s=%s' % (item[0], item[1][1:-1]))
        else:
            cookies[item[0]] = item[1]
            # print('%s=%s' % (item[0], item[1]))
    return cookies

