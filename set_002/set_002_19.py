#!/usr/bin/python
# coding: UTF-8

import sys
import re

ptn = re.compile(r'〒[\s]?([\d -]+)[\s]+([一-龠]+県)[\s]*([一-龠]+)',re.UNICODE)

lines = sys.stdin.readlines()
for line in lines:
	for elem in ptn.findall(line):
		print "\t".join(elem)



 


