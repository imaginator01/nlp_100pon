#!/usr/bin/python
# coding: UTF-8

with open('col1.txt') as c1_f:
	col1_lines = c1_f.read().split('\n')

with open('col2.txt') as c2_f:
	col2_lines = c2_f.read().split('\n')

for tmp_cols in zip(col1_lines,col2_lines):
	print '\t'.join(tmp_cols)


