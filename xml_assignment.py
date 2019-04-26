import urllib.request
import xml.etree.ElementTree as ET


url = 'http://py4e-data.dr-chuck.net/comments_161606.xml'
print('Retrieving: ', url)
xml_data = urllib.request.urlopen(url).read().decode()
print('Retrieved: ', len(xml_data), 'characters')
xml_tree = ET.fromstring(xml_data)
sum_count = 0
c = 0
for count in xml_tree.findall('.//count'):
	sum_count = sum_count + float(count.text)
	c = c+ 1
print('Count: ',c)	
print('Sum: ',sum_count)	

'''
# Alternate method
count_sum = 0
for child in xml_tree.findall('comments/comment/count'):
	count = float(child.text)
	count_sum = count_sum + count
print ('Sum of comment counts = ',count_sum)	
'''