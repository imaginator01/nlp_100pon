#!/usr/bin/python
# coding: UTF-8

import sys

word_dict={}
for line in sys.stdin:
	tmp_list = line.split('\t') 
	if len(tmp_list)>1:
		tmp_key = tmp_list[1].strip()
		tmp_val = tmp_list[0].strip() 
		if word_dict.get(tmp_key) is None:
			word_dict[tmp_key] = []
		word_dict[tmp_key].append(tmp_val)

for key in sorted(word_dict.keys(),reverse=True):
	for first_col_val in sorted(word_dict[key],reverse=True):
		print first_col_val + "\t" + key






