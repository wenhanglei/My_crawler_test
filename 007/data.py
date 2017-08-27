#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
定义用于保存数据的数据结构
"""

class Data():
    def __init__(self, title='', author='', votes=0, link=''):
        self.title = title
        self.author = author
        self.votes = votes
        self.link = link