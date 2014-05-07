#!/usr/bin/python
# coding: UTF-8

with open('address.txt') as f:
	print len(f.read().split('\n'))

