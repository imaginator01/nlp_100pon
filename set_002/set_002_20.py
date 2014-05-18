#!/usr/bin/python
# coding: UTF-8

import sys
import re

_au = ur'\ue468-\ue5df\uea80-\ueb88'
_docomo = ur'\ue63e-\ue6a5\ue6ac-\ue6ae\ue6b1-\ue6ba\ue6ce-\ue757'
_softbank = ur'\ue001-\ue05a\ue101-\ue15a\ue201-\ue253\ue301-\ue34d\ue401-\ue44c\ue501-\ue537'
_emobile = ur'%s\ue600-\ue619' % _docomo

au = re.compile(u'[%s]' % _au)
docomo = re.compile(u'[%s]' % _docomo)
softbanck = re.compile(u'[%s]' % _softbank)
emobile = re.compile(u'[%s]' % _emobile)


lines = sys.stdin.readlines()
for line in lines:
	for elem in docomo.findall(line):
		print elem



 


