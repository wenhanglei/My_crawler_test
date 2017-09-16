#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from io import StringIO
# jsn = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
# jsn = json.dumps("\"foo\bar")
# jsn = json.dumps("\u1234")
# print(jsn)
# io = StringIO()
# json.dump([1,3,4,8], io)
# print(io.getvalue())
a = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(type(a))




















