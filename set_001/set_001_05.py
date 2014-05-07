#!/usr/bin/python
# coding: UTF-8

import sys

lines = sys.stdin.readlines()
max = int(sys.argv[1])
for i in range(max):
	print (lines[i]).strip()

