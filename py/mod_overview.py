#! /usr/bin/env python2.7
from bs4 import BeautifulSoup

def printStats(gl , soup):
	# Start parsing the contents of html
	# 2) get the data for the quick stats
	try:
		statsNuggets = soup.find_all(id="stats-nuggets")[0].find_all('li')
		today = [(statsNuggets[0].h3.string).encode('utf-8'), (statsNuggets[0].span.string).encode('utf-8')]
		bestever = [(statsNuggets[1].h3.string).encode('utf-8'), (statsNuggets[1].span.string).encode('utf-8')]
		allTime = [(statsNuggets[2].h3.string).encode('utf-8'), (statsNuggets[2].span.string).encode('utf-8')]

		# 2.1) Print Quickstats for conky
		print('${font Arial:bold:size=10}'+gl.topicCol+'OVERVIEW '+gl.topicLineCol+'${hr 2}')
	except:
		pass

	try:
		print('$font'+gl.textCol+ today[0] + ' $alignr ' + gl.numCol + today[1])
		print(gl.textCol+bestever[0] + ' $alignr ' + gl.numCol + bestever[1])
		print(gl.textCol+allTime[0] + ' $alignr ' + gl.numCol + allTime[1])
	except:
		pass
	print(gl.secOffset)
	return
