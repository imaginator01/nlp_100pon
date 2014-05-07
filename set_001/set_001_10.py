#!/usr/bin/python
# coding: UTF-8

with open('col2.txt') as c2_f:
	col2_lines = c2_f.read().split('\n')

word_freq_tbl={}
for tmp_col in col2_lines:
	tmp_key = tmp_col.rstrip()
	if word_freq_tbl.get(tmp_key) is None:
		word_freq_tbl[tmp_key]=0
	word_freq_tbl[tmp_key]+=1

for k, v in sorted(word_freq_tbl.items(), key=lambda x:x[1], reverse = True):
	print k, v




