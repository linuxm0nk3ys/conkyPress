#! /usr/bin/env python2.7
import os
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
