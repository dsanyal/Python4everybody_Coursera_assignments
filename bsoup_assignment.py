'''
Scraping Numbers from HTML using BeautifulSoup In this assignment 
you will write a Python program similar to 
http://www.py4e.com/code3/urllink2.py. The program will use urllib 
to read the HTML from the data files below, and parse the data, 
extracting numbers and compute the sum of the numbers in the file.
'''
import urllib
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_161604.html'
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')
span_tags = soup('span')
num_sum = 0
for tag in span_tags:
	num_sum = num_sum + float(tag.contents[0])
#	print(tag)
print(num_sum)