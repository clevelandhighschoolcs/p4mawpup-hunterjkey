#My Webscraper File
#

from datetime import date
from datetime import time
from datetime import datetime
import time 
import urllib2
import requests

try:
	from bs4 import BeautifulSoup
except Exception:
	print "Unless you have BeautifulSoup downloaded, this program won't function" 
	print "correctly. Use 'pip install BeautifulSoup4' to download it" 
	print "(ideally in a virtual environment). You can also access more information at" 
	print "'https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe'"
	quit()
try:
	from twilio.rest import Client
except Exception:
	print "Unless you have Twilio downloaded, this program won't function" 
	print "correctly. Use 'pip install Twilio' to download it" 
	print "(ideally in a virtual environment)."
	quit()

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

#Twilio Variables \/
global Twillo_null
Twillo_null = False
global account_sid 
global auth_token
global twilio_phone_number
global my_phone_number
#Twilio Variables /\

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

#------------\/---------TWILIO------------\/---------#
print ''
#These next 20 lines have to do with Twillo and allowing that to work
print ' '
print "Would you like me to send you a text message when I find a change(y/n)? (You will need to gave a Twilio number for this to work.)"
txtmessage = raw_input()
if txtmessage == "y":
	print ' '
	print 'Enter your account SID (all of the following can be obtained on your Twilio dashboard)'
    
	account_sid1 = raw_input() 
	account_sid = "ACe11cb49076bb7e45eec7ebf2d369c8d1"
	
	print ' '
	print 'Enter your authentification token'
	auth_token1 = raw_input()
	auth_token = "92808e68d1f0ce2f8f172124a8f1a176"

	print ' '
	print 'Enter your Twillo phone number'
	twilio_phone_number1 = raw_input()
	twilio_phone_number = "7028033640"
	if (twilio_phone_number[:2] != "+1"): #this ensures a "+1" is given at the beginning of the phone number
		twilio_phone_number = "+1" + twilio_phone_number
	
	print ' '
	print "Enter your own phone number"
	my_phone_number1 = raw_input()
	my_phone_number= "+14044587197"
	if (my_phone_number[:2] != "+1"): #this ensures a "+1" is given at the beginning of the phone number
		my_phone_number = "+1" + my_phone_number
	
	#This makes sure that the info inputted is valid, if not, it skips this part.
	if (len(account_sid) != 34) or (len(auth_token) != 32) or (len(twilio_phone_number) != 12) or (len(my_phone_number) != 12) or (twilio_phone_number[:2] != "+1") or (my_phone_number[:2] != "+1"):
		Twillo_null = True #if this is triggered, the program will refrain from doing anything with the information given above
		
else:
	Twilio_null = True
#------------/\---------TWILIO------------/\---------#

print " "
print " "

def characCount():
	global prevdatastr
	global Twilio_null
	global account_sid 
	global auth_token
	global twilio_phone_number
	global my_phone_number
	
	# open a connection to the URL
	#webUrl = urllib2.urlopen(lnk)
 	try:
		webUrl = urllib2.urlopen(lnk)
	except Exception:
		print "There is an error in scraping your websites. Check to make sure your website is valid and try again."
		quit()
	if(webUrl.getcode() == 200):
		data = webUrl.read()
	else:
		print "There is an error in scraping your websites. Check to make sure your website is valid and try again."
		quit()
  # get the result code and print it, this isn't applicable in a Scraper but might as well kep it for refernxe
	#print str(webUrl.getcode())
  
  # read the data from the URL and print it
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
			Charac_Count_Body = "The website hasn't changed since you last checked it."
		else:
			print "The website has changed in some manner."
			Charac_Count_Body = "The website has changed in some manner."
		
		#Code for sending the text message
		if Twilio_null == False:
			client = Client(account_sid, auth_token)
			client.messages.create(
				body=Charac_Count_Body,
				to=my_phone_number,
				from_=twilio_phone_number
			)
	prevdatastr = len(datastr)

def Beaut():
	global prevdivstr
	global yes
	global null
	global Twilio_null
	global account_sid 
	global auth_token
	global twilio_phone_number
	global my_phone_number
	
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
			print "This program returned 'None' as the value of the <p>. Therefore, this program"
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
				BeautBody = "The first <p> in this website has remained the same since this program last checked it."
			else:
				print "This <p> and/or something inside of it has changed since this program last"
				print "updated."
				BeautBody = "This <p> and/or something inside of it has changed since this program last updated."
			
			#This code sends the text message
			if Twillo_null == False:
				client = Client(account_sid, auth_token)
				client.messages.create(
					body=BeautBody,
					to=my_phone_number,
					from_=twilio_phone_number
				)
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

