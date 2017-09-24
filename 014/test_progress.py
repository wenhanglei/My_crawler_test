#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util
import time

util.print_progress(0,100,'progress','complete',length=50)
for i in range(100):
    time.sleep(0.1)
    util.print_progress(i+1, 100, 'progress','complete',length=50)