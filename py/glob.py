#! /usr/bin/env python2.7
import os
import re
from bs4 import BeautifulSoup

path = os.path.normcase(os.path.dirname(os.path.realpath(__file__))+'/')
conf = BeautifulSoup(open(path+"../config.xml", "r"))
pathHtml = path + '../data/data.html'
pathHtml2 = path + '../data/data2.html'
imageDir = path+'../data/'

secOffset = ('${voffset '+str(abs(int(conf.sectionoffset.string)))+'}').encode('utf-8')
topicCol = '${color '+(conf.topiccolor.string).encode('utf-8')+'}'
topicLineCol = '${color '+(conf.topiclinecolor.string).encode('utf-8')+'}'
textCol = '${color '+(conf.textcolor.string).encode('utf-8')+'}'
numCol = '${color '+(conf.numbercolor.string).encode('utf-8')+'}'
noimages = (conf.noimages.string).encode('utf-8')
maxTextLen = int((conf.maxtextlength.string).encode('utf-8'))
remove_str_list = conf.find_all("remove")

def removeNonAscii(s): 
	res="";
	privious=""
	for i in s:
		if ord(i)>31 and ord(i)<128:
			res=res+i
			privious=i
		elif privious!=' ':
			res=res+' '
			privious=' '
	return res

def removeSubstring(sublist, string): 
	res = string
	for s in sublist:
		sub = (s.string).encode('utf-8')
		length = len(sub)
		shift = 0
		indexlist = [m.start() for m in re.finditer(sub, res)]
		for i in indexlist:
			res=res[i-shift+length:]
			shift = shift+i+length
	return res
