#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()

rp.set_url('https://www.zhihu.com/robots.txt')

rp.read()

print(rp.can_fetch('badcralwer', '/logout'))