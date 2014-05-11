#!/usr/bin/python
# coding: UTF-8

import sys
import re

ptn = re.compile(r'(.*)RT @')
for line in sys.stdin:
	m= ptn.match(line)
	if m:
		print m.group(1)


