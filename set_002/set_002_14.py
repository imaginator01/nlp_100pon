#!/usr/bin/python
# coding: UTF-8

import sys
import re

ptn = re.compile(r'@[^(\s)]+',re.UNICODE)
for line in sys.stdin:
	for elem in ptn.findall(line):
		print elem



