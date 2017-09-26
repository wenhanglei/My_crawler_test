#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util
import pymysql
import requests
import sqlutil
from bs4 import BeautifulSoup

class PageNummberWrong(Exception):
    def __init__(self):
        super()

class ShanbayCrawer:
    def __init__(self, connection):
        """
        初始化函数
        :param connection: 用于保存数据的数据库连接对象
        """
        #数据库连接对象
        self.connection = connection
        #访问入口
        self.entry = 'https://www.shanbay.com/checkin/user/20272978'
        #包含user-agent的header
        self.header = util.load_header('../header.txt')
        #用于访问目标的cookies
        self.cookies = util.get_cookie_dic_from_file('cookie.txt')
        self.cursor = connection.cursor()

    def save_study_data(self, first, last):
        """
        获取时间数据保存到数据库
        :param first: 起始页码(int)
        :param last:  结束页码(int)
        :return: 
        """
        #遍历输入页面
        if first >= 0 and last >= first:
            util.print_progress(0, 10*(last-first+1),'download', 'complete',length=40)
            for num in range(first, last+1):
                url_tail = '' if first == 0 else '?page=' + str(num)
                #访问地址
                url = self.entry + url_tail
                #获取响应
                resp = requests.get(url, headers=self.header, cookies=self.cookies)
                # 创建BeautifulSoup对象
                bsobj = BeautifulSoup(resp.text, 'html.parser')
                # 获取包含数据的容器
                ctans = bsobj.find_all('div', class_='span7 content')
                for n, ctan in enumerate(ctans):
                    text = ctan.find('div', class_='note').string.strip()
                    date = ctan.find('div', class_='span4').string.strip()
                    d_time = util.convert_timeformat(date)
                    # 保存记录
                    sqlutil.insert(self.cursor, 'study', text, d_time)
                    #显示进度
                    util.print_progress((num-first)*10+n+1, 10*(last-first+1), 'download', 'complete', length=40)
                self.connection.commit()
            self.connection.close()
        else:
            raise PageNummberWrong()


    def test(self):
        raise PageNummberWrong()

if __name__ == '__main__':
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='*****',
                                 db='test',
                                 charset='utf8')
    ShanbayCrawer(connection).save_study_data(21, 87)

