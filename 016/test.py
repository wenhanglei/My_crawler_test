#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test(i = 5):
    try:
        if(i == 0):
            return 100
        else:
            raise Exception('something wrong')
    except Exception as e:
        return test(i-1)

test()