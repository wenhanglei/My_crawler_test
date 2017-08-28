#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle

with open('answer_links.pkl', 'rb') as file:
    data = pickle.load(file)
    for item in data:
        print('%s : %s' % (item.title, item.link))