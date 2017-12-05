#My Webscraper File
#

from datetime import date
from datetime import time
from datetime import datetime
import time 
import urllib2
from bs4 import BeautifulSoup

print " "
print "-------------------------------------------------------------------------------"
print "X    X  XXXXXX  XXXXX    XXXXXX  XXXXXX  XXXXX    XXXX   XXXXX   XXXXXX  XXXXX"
print "X    X  X       X    X   X       X       X   XX  X    X  X    X  X       X   XX"
print "X XX X  XXXXXX  XXXXX    XXXXXX  X       XXXXX   XXXXXX  XXXXX   XXXXXX  XXXXX"
print "XX  XX  X       X    X        X  X       X  XX   X    X  X       X       X  XX"
print "X    X  XXXXXX  XXXXX    XXXXXX  XXXXXX  X   XX  X    X  X       XXXXXX  X   XX"
print "-------------------------------------------------------------------------------"

print " "
print "By: Hunter Key, Period 4"
print " "

print "Unless you have BeautifulSoup downloaded, this program won't function" 
print "correctly. Use 'pip install BeautifulSoup4' to download it" 
print "(ideally in a virtual environment). You can also access more information at" 
print "'https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe'"

print " "
print "this program analyzes the changes to a website's total character count and a " 
print "website's first <p> (paragrpah) tag during an interval and period of seconds " 
print "you define. After that you will have to restart the program."
print " "

global cnt
cnt = 0
#These next 4 lines are to ensure that my program doesn't shut down the first time it runs through the webpage
global prevdatastr
prevdatastr = "0"
global prevdivstr
prevdivstr = "0"

#this value checks to make sure that Beaut() doesn't return null
global null
null = 0

print "For the link that you give this program, ensure that this link" 
print "begins with a 'https,' otherwise, the program will not be able to" 
print "access the website and this program will only return an error.)"
print " "
lnk = raw_input("Enter your Link: ")
inter = int(raw_input("How many times (interval) do you want me to remonitor your site?: "))
tm = int(raw_input("How many seconds do you want me to wait until I remonitor your site?: "))

print " "
print " "


def characCount():
	global prevdatastr
	
	# open a connection to the URL
	webUrl = urllib2.urlopen(lnk)
  
  # get the result code and print it, this isn't applicable in a Scraper but might as well kep it for refernxe
	#print str(webUrl.getcode())
  
  # read the data from the URL and print it
	data = webUrl.read()
	datastr = str(data)
	
	#this if statement checks to see if this isn't the first time we open the webpage
	if (cnt == 0):
		print "Finding base site to moniter."
	
	
	if (cnt >= 1):
		now = datetime.now()
		print now.strftime("%a, %B %dth, %Y"), "at", now.strftime("%I:%M:%S %p")
		print " "
		print "there are",len(datastr),"characters in the HTML code of this current webpage."
		if prevdatastr == len(datastr):
			print "The website hasn't changed since you last checked it."
		else:
			print "The website has changed in some manner."
	
	prevdatastr = len(datastr)
	
def Beaut():
	global prevdivstr
	global yes
	global null
	
	#query the website and return the html to the variable page
	page = urllib2.urlopen(lnk)
	
	# parse the html using beautiful soap and store in variable `soup`
	soup = BeautifulSoup(page, "html.parser")
	
	# Take out the <p> of name and get its value
	name_box = soup.find("p", attrs={"class": ""})
	#print name_box

	if (name_box != None):
		name = name_box.text.strip() # strip() is used to remove starting and trailing
		#print name
	else:
		name = 1
		
	if (cnt == 0):
		if (name == 1):
			print "This programmed returned 'None' as the value of the <p>. Therefore, this program"
			print "will not be able to accuratly give you an answer for this aspect of the website."
			print "For the remainder of this scraping, we will stop checking for this."
			null = 1
	if (null == 0):
		#this if statement checks to see if this isn't the first time we open the webpage
		if (cnt >= 1):
			print " "
			if (prevdivstr == name):
				print "The first <p> in this website has remained the same since this program last"
				print "checked it."
			else:
				print "This <p> and/or something inside of it has changed since this program last"
				print "updated."
		prevdivstr = name

while(cnt <= inter):
	print "-----------------------------------------------------------------------------"
	characCount()
	Beaut()
	print "-----------------------------------------------------------------------------"
	cnt += 1
	print " "
	print " "
	time.sleep(tm)
	
print "Thank you for using Hunter Key's WebScraper!"
print " "
print " "
