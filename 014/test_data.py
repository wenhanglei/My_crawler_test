#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util
import pymysql

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

    def save_study_data(self, first, last):
        """
        获取时间数据保存到数据库
        :param first: 起始页码(int)
        :param last:  结束页码(int)
        :return: 
        """
        #遍历输入页面
        if first >= 0 and last >= first:
            pass
        else:
            raise PageNummberWrong()


    def test(self):
        raise PageNummberWrong()

if __name__ == '__main__':
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='****',
                                 db='test',
                                 charset='utf8')
    ShanbayCrawer(connection).test()

