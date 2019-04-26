import urllib.request
import json

url = 'http://py4e-data.dr-chuck.net/comments_161607.json'
print('Retrieving', url)

data = urllib.request.urlopen(url).read().decode()
print('Retrieved',len(data), 'characters')
json_data = json.loads(data)

print('Count: ', len(json_data['comments']))

sum_comments = 0
for comment in json_data['comments']:
	sum_comments = sum_comments + comment['count']
print('Sum: ', sum_comments)	
