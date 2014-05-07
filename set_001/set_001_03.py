#!/usr/bin/python
# coding: UTF-8

import sys

c1_f = open('col1.txt','w')
c2_f = open('col2.txt','w')

for line in sys.stdin:
	tmp_list = line.split('\t')
	c1_f.write(tmp_list[0].rstrip() + '\n')			
	if len(tmp_list)>1:
		c2_f.write(tmp_list[1].rstrip() + '\n')			

c1_f.close()
c2_f.close()

