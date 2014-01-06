#! /usr/bin/env python2.7
from bs4 import BeautifulSoup

def printStats(gl, soup, adminPageEx):
	if adminPageEx == 'true':
		print('${font Arial:bold:size=10}'+ gl.topicCol +'COMMENTS '+gl.topicLineCol+'${hr 2}')
		print('${color red}Error getting comment stats')
		print(gl.secOffset)
	else:
		#Private variables
		pendingCol = '${color '+(gl.conf.pendingcolor.string).encode('utf-8')+'}'
		spamCol = '${color '+(gl.conf.spamcolor.string).encode('utf-8')+'}'
		secondaryCol = gl.textCol
		maxTextLen = int((gl.conf.maxtextlength.string).encode('utf-8'))
		
		approved = '0'
		pending = '0'
		spam = '0'
		commStats = []

		# Start parsing the contents of html
		#Collects the 
		try:
			approved = (soup.find("input", { "name" : "_total" })['value']).encode('utf-8')
		except:
			pass

		try:
			pending = (soup.find("span", { "class" : "pending-count" }).string).encode('utf-8')
		except:
			pass

		try:
			spam = (soup.find("span", { "class" : "spam-count" }).string).encode('utf-8')
		except:
			pass

		commStats = [['Approved',str(int(approved)-int(pending))], ['Pending',pending], ['Spam', spam]]

		# Display the comments stats in the correct color
		if len(commStats)>=1:
			cnt=0
			print('${font Arial:bold:size=10}' + gl.topicCol + 'COMMENTS '+ gl.topicLineCol + '${hr 2}')
			for c in commStats:
				if(len(c)==2):
					if(cnt==1):
						secondaryCol=pendingCol			
					elif(cnt==2):
						secondaryCol=spamCol
					else:
						secondaryCol=gl.numCol
					cnt+=1
					if(c[1]=='0'):
						print('$font' + gl.textCol+ c[0] +'$alignr '+ gl.numCol + c[1])
					else:						
						print('$font' + gl.textCol+ c[0] +'$alignr '+ secondaryCol + c[1])
			print(gl.secOffset)

	return
