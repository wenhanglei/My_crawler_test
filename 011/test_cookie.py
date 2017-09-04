#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util

co_li = util.load_obj('cookies.pkl')
cookies = util.get_cookie_dir(co_li)
print(cookies)
