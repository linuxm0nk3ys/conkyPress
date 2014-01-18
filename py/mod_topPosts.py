#! /usr/bin/env python2.7
from bs4 import BeautifulSoup

def printStats(gl, soup):
	#Private variables
	highTxColor = '${color '+(gl.conf.mytextcolor.string).encode('utf-8')+'}'
	highNumCol = '${color '+(gl.conf.mynumbercolor.string).encode('utf-8')+'}'
	postStats = []
	rawPosts = []
	myPosts = []

	# Start parsing the contents of html
	try:
		#find the table with the users posts
		posts =soup.find("div", { "id" : "postviews" }, { "class" : "postbox" }).find("div", {"class" : "today"}).find("table", {"class" : "statsDay"})
		# assume we found the table with the posts
		rawPosts = posts.find_all("tr")
	except:
		pass

	try:
		################## BEGIN OF DUPLICATED CODE ###################
		# This code was imported from mod_myTopPosts
		# Its used to find the users own posts in the top-Posts list
		# It should be removed from here and accessed from a file with global vars and functions

		#find the table with the users posts
		myAutherName = (soup.find("span", {"class" : "ab-display-name"}).string).encode('utf-8')
		authViewToday = soup.find("div", { "id" : "authorviews" }, { "class" : "postbox" }).find("div", { "class" : "today" })
		authorList = authViewToday.find_all("td", { "class" :"label-avatar"})

		author=''
		for auth in authorList:	
			if auth.span.string.lower() == myAutherName.lower():
				author=auth.span
				while (str(author)).find('<tr class="table"') == -1:
					author=author.next_element

		rp =author.find_all("tr")
		if not rp == []:
			for p in rp:
				myPosts = myPosts+[((p.a.string).encode('utf-8'), (p.find("td", {"class" : "views"}).string).encode('utf-8'))]
		################## END OF DUPLICATED CODE ######################
	except:
		pass

	
	if len(rawPosts)>1:
		rawPosts=rawPosts[1:len(rawPosts)]

	if not rawPosts == []:
		for p in rawPosts:
			try:
				postStats = postStats+[((p.a.string).encode('utf-8'), (p.find("td", {"class" : "views"}).string).encode('utf-8'))]
			except:
				pass 
		# 3.1) print the Author-Top-Posts for Conky
		print('${font Arial:bold:size=10}'+ gl.topicCol +'ALL-TOP-POSTS '+gl.topicLineCol+'${hr 2}')
		for p in postStats:
			name=gl.removeSubstring(gl.remove_str_list ,gl.removeNonAscii(p[0]))
			if len(name)>gl.maxTextLen:
				name=name[0:gl.maxTextLen]+"..."
			# also color own posts differently
			useTxCol = gl.textCol
			useNumCol = gl.numCol
			for m in myPosts:
				# this is still ugly
				if ''.join(e for e in p[0] if e.isalnum())  == ''.join(e for e in m[0] if e.isalnum()):
					useTxCol = highTxColor
					useNumCol = highNumCol
					break
			print('$font'+useTxCol+ name +'$alignr '+ useNumCol + p[1])
		print(gl.secOffset)
	return
