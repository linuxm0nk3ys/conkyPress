#! /usr/bin/env python2.7
import time
from bs4 import BeautifulSoup

def printStats(gl , soup, loginEx):
	#Private variables
	titleCol = '${color '+(gl.conf.titlecolor.string).encode('utf-8')+'}'
	timeCol = '${color '+(gl.conf.timecolor.string).encode('utf-8')+'}'
	setlogo = (gl.conf.conkypresslogo.string).encode('utf-8')
	localtime = time.asctime( time.localtime(time.time()) )
	hOffset = ('${offset 0}').encode('utf-8')
	vOffset = ('${voffset 0}').encode('utf-8')
	vOffsetTit = ('${voffset 15}').encode('utf-8')
	logoDim = ('55').encode('utf-8')

	if setlogo.lower() == 'true' and gl.noimages.lower() != 'true':
		hOffset = ('${offset 75}').encode('utf-8')
		vOffset = ('${voffset 12}').encode('utf-8')

	# Start parsing the contents of html
	# 1) get the page title
	# but dont get it from the title tag
	try:
		title = (soup.find_all("meta", {"name" : "application-name"})[0]['content']).encode('utf-8')
	except:
		pass

	# 1.1) Print title for conky and add offset
	try:
		print(vOffsetTit+hOffset+'${font Arial:bold:size=18}'+titleCol+title)
		print(vOffset+'${font}'+timeCol+'Last Update: ' + localtime)
	except:
		pass
	if setlogo.lower() == 'true' and gl.noimages.lower() != 'true':
		print('${image '+gl.path+'../data/cp_logo.png -p 0,0 -s '+logoDim+'x'+logoDim+'}')

	# Finally Check for login error
	if loginEx.lower() == 'true':
		print('${voffset 0}${color red}Warning: no connection or wrong credentials')
	return
