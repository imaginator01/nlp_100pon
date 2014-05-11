#!/usr/bin/python
# coding: UTF-8

import sys
import re

ptn = re.compile(r'.*なう$')
for line in sys.stdin:
	if ptn.match(line):
		print line

