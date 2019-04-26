import urllib
import re
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/known_by_Joshiah.html'
html = urllib.request.urlopen(url).read()

position = 18
for i in range(7):
	soup = BeautifulSoup(html, 'html.parser')
	anchor_tags = soup('a')
	links = [tag.get('href') for tag in anchor_tags ]
	print('Retrieving:', links[position-1])
	html = urllib.request.urlopen(links[position-1]).read()
#print('Last name in sequence: ',links[position-1].split('_')[2].split('.')[0])	
print('Last name in sequence: ',re.findall('by_(\S+)\.html', links[position-1])[0])	