#! /usr/bin/env python2.7
from bs4 import BeautifulSoup

def printStats(gl, soup):
	#Private variables
	myAutherName = ''
	rawPosts = []
	postStats = []
	myTotalViews = 0	
	sumOfShown = 0

	# Start parsing the contents of html
	#find the table with the users posts
	try:
		myAutherName = (soup.find("span", {"class" : "ab-display-name"}).string).encode('utf-8')
		authViewToday = soup.find("div", { "id" : "authorviews" }, { "class" : "postbox" }).find("div", { "class" : "today" })
		authorList = authViewToday.find_all("td", { "class" :"label-avatar"})

		author=''
		for auth in authorList:	
			if auth.span.string.lower() == myAutherName.lower():
				author=auth.span
				while (str(author)).find('<tr class="table"') == -1:
					author=author.next_element
					# try to get the total views of the user
					try:
						if (str(author)).find('<td class="views"') != -1:
							myTotalViews = int(author.string)
					except:
						pass
		# assume we found the table with the posts
		rawPosts = author.find_all("tr")
	except:
		pass


	if not rawPosts == []:
		for p in rawPosts:
			postStats = postStats+[((p.a.string).encode('utf-8'), (p.find("td", {"class" : "views"}).string).encode('utf-8'))]
		# 3.1) print the Author-Top-Posts for Conky
		print('${font Arial:bold:size=10}'+gl.topicCol+'MY-TOP-POSTS '+gl.topicLineCol+'${hr 2}')
		for p in postStats:
			name=gl.removeSubstring(gl.remove_str_list ,p[0])
			if len(name)>gl.maxTextLen:
				name=name[0:gl.maxTextLen]+"..."
			print('$font'+gl.textCol+ name +'$alignr '+gl.numCol+ p[1])
			# sum the number of clicks of each post			
			try:
				sumOfShown = sumOfShown+int(p[1])
			except:
				pass
		
		# There are to many posts to show them all, so lets show the remaining clicks
		try:		
			if sumOfShown < myTotalViews:
				print('$font'+gl.textCol+ 'Other posts' +'$alignr '+gl.numCol+ str(myTotalViews - sumOfShown))
		except:
			pass

		print(gl.secOffset)
	return
