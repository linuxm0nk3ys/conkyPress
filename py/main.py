#! /usr/bin/env python2.7
import glob, login, mod_title, mod_overview, mod_authors, mod_comments, mod_myTopPosts, mod_topPosts
from bs4 import BeautifulSoup

titlEnabled = (glob.conf.title.string).encode('utf-8')
overEnabled = (glob.conf.overview.string).encode('utf-8')
commEnabled = (glob.conf.comments.string).encode('utf-8')
authEnabled = (glob.conf.authors.string).encode('utf-8')
mTopEnabled = (glob.conf.mytopposts.string).encode('utf-8')
topPEnabled = (glob.conf.alltopposts.string).encode('utf-8')

loginStatus = ['false', 'false']
loginStatus = login.perform(glob)
soup = ''
soup2 = ''

try:
	soup = BeautifulSoup(open(glob.pathHtml))
	soup2 = BeautifulSoup(open(glob.pathHtml2))
except:
	pass

if titlEnabled != 'false':
	mod_title.printStats(glob, soup, loginStatus[0])
if overEnabled != 'false':
	mod_overview.printStats(glob, soup)
if commEnabled != 'false':
	mod_comments.printStats(glob, soup2, loginStatus[1])
if authEnabled != 'false':
	mod_authors.printStats(glob, soup, loginStatus[0])
if mTopEnabled != 'false':
	mod_myTopPosts.printStats(glob, soup)
if topPEnabled != 'false':
	mod_topPosts.printStats(glob, soup)
