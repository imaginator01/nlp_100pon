#!/usr/bin/python
# coding: UTF-8

import sys
import re

ptn = re.compile(r'仙台市[\s]*[一-龠]+[\s]*[一-龠]+[\s]*[\d -]+',re.UNICODE)

lines = sys.stdin.readlines()
for line in lines:
	for elem in ptn.findall(line):
		print elem


 


