conkyPress
==========
ConkyPress a WordPress stats visualization tool for your desktop

Version: 1.0.9 (stable), 
Author : Drunk3nm0nk3y , 
Website: http://wp.me/p2nic6-eP

DOCUMENTATION - INDEX
---------------------
1) ABOUT CONKYPRESS
2) DEPENDENCIES
3) CONFIGURATION
4) STARTING & STOPPING
5) TROUBLESHOOTING
6) CHANGELOG
7) ACKNOWLEDGMENT

1. ABOUT CONKYPRESS
---------------------
conkyPress is a software written in python that utilizes conky 
to show the stats of your Wordpress blog on your desktop.

2. DEPENDENCIES
---------------------
- conky compiled with Imlib2 support
- Imlib2
- python2
- python-lib: BeautifulSoup
- python-lib: pycurl

Important: Without "Imlib2" you will have no support for 
images in conky/conkyPress. If you don't want to install Imlib2,
you have to disable the use of images in the "config.xml"
(see 3.CONFIGURATION for more Information).

3. CONFIGURATION
---------------------
Configuration of conkyPress can be done in the provided "config.xml".
The most important part is to fill in your wordpress login information 
and your blogs URL. You can also use the config.xml to: 
-- Enable or disable the differnt sections of conkyPress
-- Tweak conkyPress like correcting the position of images
-- Disable the ConkyPress-Logo
-- Disable images at all (usefull if you don't have Imlib2)
-- Change the styling/colors of conkyPress

Notice: If you know what you are doing, you can also change the 
options in the conkyPressRc

4. STARTING, STOPPING & RESTARTING
---------------------
Use the provided shell script to start/stop/restart conkyPress 
and remember to make the script executable: 
- Start conkyPress by executing conkyPress.sh like this "./conkyPress.sh start" 
- Stop conkyPress by executing conkyPress.sh like this "./conkyPress.sh stop" 
- Restart conkyPress by executing conkyPress.sh like this "./conkyPress.sh restart" 

5. TROUBLESHOOTING
---------------------
conkyPress is still very new, so in case of any trouble with the software 
you can write comment on 
http://evilshit.wordpress.com/2013/04/20/conkypress-a-wordpress-stats-visualization-tool-for-your-desktop

6. CHANGELOG
---------------------
* v1.0.9
-- Update to match the html-code changes of the wordpress stat pages. This fixes the "my top posts" section
-- Fixed typos in comments
-- Fixed typo in the README
-- ConkyPress moved from BETA to STABLE
* v1.0.8
-- Added feature, by using the config.xml it is now possible to filter words in post titels
-- Improvement, added usage Info for restarting to conkyPress.sh 
* v1.0.7
-- Improvement, replaced start/stop script by an other script. It uses parameters to start, stop or restart conkyPress
-- Fix in comments section, number of pending posts were added to number of approved posts
* v1.0.6
-- Added number of yesterdays visitors to the overview section
-- Fixed a critical typo in an elemet of the config.xml
-- Improvement, inversed order of changelog, newest version is now at top
* v1.0.5
-- Fixed/adapted parsing of the comments stats (WordPress changed some stuff)
-- Improvement, showing an "other posts" entry in the "my top posts" section if there are to many posts to display
* v1.0.4
-- Fixed character encoding in the all-top-posts section
-- Added different colors for pending and spam comments
-- Added entrys in config.xml for comment section colors
-- Improved notation of colors in the config.xml
* v1.0.3:
-- Improved stop-script, it now kills all running ConkyPress instances
-- Improvement, less memory consumption
-- Improvement, now using real transperancy
-- Made the background semitransparent for better usability on bright desktop backgrounds
-- Fix in the conkyPressRc for users who use slim and the last version of gnome3
-- Added comment for Xfce users in the conkyPressRc
-- Added comments in the conkyPressRc, for users who want to customize the look an transparency
-- Removed unnecessary options from the conkyPressRc
* v1.0.2: 
-- Fixed alignment of numbers in authors sections
-- Fixed exception in "all-top-posts" section if the user has no posts in it
-- Added option in the config.xml to set the space between the sections 
-- Removed the "-q" option in the startscript, so users can see any error messages
* v1.0.1: 
-- Fixed session login problem in login.py, leading to errors in comment section
-- Fixed some typos in the comments of conkyPressRc

7. ACKNOWLEDGMENT
---------------------
- Thanks to the conky project (http://conky.sourceforge.net/) 
for making this possible.
- A special thanks goes to h0nkym0nk3y and funkym0nk3y 
for beta-testing conkyPress, their great feedback and ideas for improvements.

