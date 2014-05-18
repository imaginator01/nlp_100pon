#!/usr/bin/python
# coding: UTF-8

import sys
import re

ptn = re.compile(r'([一-龠]+)\(([A-Z]+)\)',re.UNICODE)

lines = sys.stdin.readlines()
for line in lines:
	for elem in ptn.findall(line):
		print elem[0],"\t",elem[1]


