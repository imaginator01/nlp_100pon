#!/usr/bin/python
# coding: UTF-8

import sys
import re

ptn = re.compile(ur'([一-龠]+)\(([A-Z]+)\)',re.UNICODE)

lines = sys.stdin.readlines()
for line in lines:
	for elem in ptn.findall(unicode(line,"utf-8")):
		print elem[0],"\t",elem[1]


