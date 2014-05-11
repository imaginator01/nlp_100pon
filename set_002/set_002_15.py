#!/usr/bin/python
# coding: UTF-8

import sys
import re

ptn = re.compile(r'<a href="(.*)">.*(@[^(\s)]+).*</a>',re.UNICODE)
tmp_dict={}

lines = sys.stdin.readlines()
for line in lines:
	for elem in ptn.findall(line):
		tmp_dict[elem[1]] = elem[0]

for line in lines:
        print re.sub(r'@[^(\s)]+',lambda match_obj: tmp_dict[match_obj.group(0)] , line) 

