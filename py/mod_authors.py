#! /usr/bin/env python2.7
import urllib
import os
from bs4 import BeautifulSoup

def printStats(gl, soup, loginEx):
	#Private variables
	imgCor = int((gl.conf.imagecorrection.string).encode('utf-8'))
	imgSpCor = int((gl.conf.imagespacecorrection.string).encode('utf-8'))
	nameOffset = 0
	borderSpace = 2
	verticalSpace = 10
	imgSpace = 8+imgSpCor
	if loginEx == 'true':
		imgOffset = 255+imgCor+15
	else:
		imgOffset = 255+imgCor
	authors=[]
	# Start parsing the contents of html

	# 3) get the Authors & their images & stats
	try:
		authViewToday = soup.find("div", { "id" : "authorviews" }, { "class" : "postbox" }).find("div", { "class" : "today" })
		authorList = authViewToday.find_all("td", { "class" :"label-avatar"})
		for auth in authorList:
			#Download author images
			if not os.path.exists(gl.imageDir+auth.span.string):
				urllib.urlretrieve(auth.img['src'],gl.imageDir+auth.span.string)
			authors= authors+[(auth.span.string, auth.parent.find("td", {"class" : "views"}).string, auth.img['width'],auth.img['height'] )]
	
		if len(authors)>0 and not gl.noimages.lower() == 'true':
			nameOffset = int(authors[0][3])+(borderSpace*4)
	except:
		pass
	
	# 3.1) print the Authors-Stats for Conky
	if len(authors)>0:
		print('${font Arial:bold:size=10}'+gl.topicCol+'AUTHORS '+gl.topicLineCol+'${hr 2}')
		for a in authors:
			if gl.noimages.lower() != 'true':
				imgOffset = imgOffset + int(a[2]) + imgSpace
				print('${image '+gl.imageDir+a[0].encode('utf-8') +' -p '+str(borderSpace).encode('utf-8')+','+str(imgOffset).encode('utf-8')+' -s '+ a[2].encode('utf-8')+'x'+a[3].encode('utf-8')+'}')
			print('$font'+gl.textCol+'${offset '+ str(nameOffset).encode('utf-8')+'}'+a[0].encode('utf-8')+' $alignr '+gl.numCol+a[1].encode('utf-8')+'${voffset '+str(verticalSpace).encode('utf-8')+'}')
		print(gl.secOffset)
	return
