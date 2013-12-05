#! /usr/bin/env python2.7
import pycurl
import StringIO
import urllib
from bs4 import BeautifulSoup

def perform(glob):
	loginEx = 'false'
	adminPageEx = 'false'
	pathCookie = glob.path + '../data/cookie'

	# TODO this file should be rewritten as a class with functions/defs

	#Read the login Information
	username = (glob.conf.username.next_element).encode('utf-8')
	password = (glob.conf.password.next_element).encode('utf-8')
	loginUrl = (glob.conf.blogurl.next_element).encode('utf-8')+'/wp-login.php'
	redirectUrl_admin = (glob.conf.blogurl.next_element).encode('utf-8')+'/wp-admin/'
	redirectUrl_stats = redirectUrl_admin + '?page=stats'
	redirectUrl_comments = redirectUrl_admin + 'edit-comments.php'

	#Create the POST-String for login
	post_string_encoded = urllib.urlencode({'log' : username, 'pwd' : password, 'wp-submit': 'Log In' , 'redirect_to' : redirectUrl_stats, 'testcookie' : 1})
	post_string_encoded_comments = urllib.urlencode({'log' : username, 'pwd' : password, 'wp-submit': 'Log In' , 'redirect_to' : redirectUrl_comments, 'testcookie' : 1})

	#Create a buffer and instantiate pycurl
	buf = StringIO.StringIO()
	c = pycurl.Curl()

	#create cookie, login and write everything to buffer
	try:
		c.setopt(pycurl.COOKIEJAR, pathCookie)
		c.setopt(c.URL, loginUrl)
		# lets throw the results away
		c.setopt(pycurl.WRITEFUNCTION, lambda x: None) 
		c.setopt(pycurl.FOLLOWLOCATION, 1)
		c.setopt(c.CONNECTTIMEOUT, 10)
		c.setopt(c.TIMEOUT, 15)
		c.setopt(c.FAILONERROR, True)
		c.setopt(c.VERBOSE, False)
		c.setopt(c.HTTPHEADER, ['Accept: text/html', 'Accept-Charset: UTF-8'])
		c.perform()
	except pycurl.error, error:
		errno, errstr = error

	try:
		buf.truncate(0);
		c.setopt(pycurl.WRITEFUNCTION, buf.write)
		c.setopt(c.VERBOSE, False)
		c.setopt(pycurl.COOKIEFILE, pathCookie)
		c.setopt(c.URL, loginUrl)
		c.setopt(c.POSTFIELDS, post_string_encoded)
		c.setopt(pycurl.FOLLOWLOCATION, 1)
		c.perform()
	except:
		loginEx = 'true'
	else:
		try:
			soup = BeautifulSoup(buf.getvalue())
			if soup.find("div",{"id":"login_error"}) is None:	
				# create a new file or overwrite an existing file
				f = open(glob.pathHtml, "w")
				# Write a sequence of strings to a file
				f.writelines(buf.getvalue())
				f.close()
			else:
				loginEx = 'true'			
		except IOError:
			#print('${color red} Error writing data to filesystem')
			pass			
		finally:
			buf.close()

	# Try to get the admin page for the comments section
	if loginEx != 'true':
		buf = StringIO.StringIO()
		try:
			buf.truncate(0);
			c.setopt(pycurl.WRITEFUNCTION, buf.write)
			c.setopt(pycurl.COOKIEFILE, pathCookie)
			c.setopt(c.VERBOSE, False)
			c.setopt(c.URL, loginUrl)
			c.setopt(c.POSTFIELDS, post_string_encoded_comments)
			c.setopt(pycurl.FOLLOWLOCATION, 1)
			c.perform()
		except:
			adminPageEx = 'true'
		else:
			try:
				f = open(glob.pathHtml2, "w")
				f.writelines(buf.getvalue())
				f.close()
			except:
				adminPageEx = 'true'
				pass			
			finally:
				buf.close()
	return [loginEx, adminPageEx]
