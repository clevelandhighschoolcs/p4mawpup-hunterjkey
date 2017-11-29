# Hunter Key's Website Scraper
This Program takes the HTML code from a website that you gives it and chacks for changes in the number of characters within the whole HTML 
code, and for changes within the first div tag of that website. This program isn't very good at looking at specific and numerous aspects 
of a site, but as long as the website is secure (i.e. "https://"), the program can scrape it.

I pulled code from https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe, along with Walker's 
Datetime and Webdata snippets into my final product. 


# Instructions:
===============================================================================

1) You NEED to have Python 2.7.14 downloaded on your computer.
2) Unless you have one you want to use, create a folder on your desktop and create a virtual envirenment within it. Thic cna be done by typing/pasting "" into the command line while in your folder.
3) Leave the virtual envirenment alone for now and paste WebScraper.py (the other folder in this repository) into a Notepad++ document and save it into the folder that has your virtual environment under a name of your choice ("HunterWebScraper.py" is a good choice). ANYWHERE ELSE AND IT WON'T WORK.
4) Open the virtual envirenment that houses Webscraper.py, open your virtual environment in the command line, and type/paste "pip install BeautifulSoup4" into the command line. This downloads BeautfulSoup, a python library that is essential to the functionality of this program.
5) Wait for it to download.
6) Type "python HunterWebScraper.py" (or whatever you named my file on your computer) into the command line. Do not include any other parameters, this will only lead to an error) and press enter.
7) A screen will appear detailing my Web Scraper and how it works. A input will appear at the bottom asking for a link, ensure that the link that you enter starts with an "https://" because otherwise, you will encounter an error along the lines of "HTML forbidden." Enter the link and press enter.
8) There are two more inputs after this, one for the number of times the program runs and one for the time it waits between scaping, enter a value for each of these.
9) If all the previous steps were followed correctly, the Scraper will begin running and scrape the website per your parameters.
