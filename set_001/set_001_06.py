#!/usr/bin/python
# coding: UTF-8

import sys

num = int(sys.argv[1])
lines = sys.stdin.readlines()[-num:]
for line in lines:
        print line.strip()


