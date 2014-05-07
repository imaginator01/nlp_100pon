#!/usr/bin/python
# coding: UTF-8

import sys

word_dict={}
for line in sys.stdin:
	word_dict[line.split('\t')[0]] = True
print len(word_dict.keys())



