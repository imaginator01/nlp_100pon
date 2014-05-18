#!/usr/bin/python
# coding: UTF-8

import sys
import re

ptn = re.compile(r'[一-龠 \w]+さん',re.UNICODE)

lines = sys.stdin.readlines()
for line in lines:
	for elem in ptn.findall(line):
		print elem


 


