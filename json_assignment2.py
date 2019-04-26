import json, urllib, ssl


location = 'University of Dallas'
print('Location: ', location)
api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
param = {}
param['address'] = location
param['key'] = api_key
url = serviceurl + urllib.parse.urlencode(param)

# Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE


data = urllib.request.urlopen(url).read().decode()
print('Retrieved',len(data), 'characters')
try:
	json_data = json.loads(data)
except:
	json_data = None	

if json_data and json_data['status'] == 'OK' :	
	print('Place id: ',json_data['results'][0]['place_id'])	
else:
	print('---------Failed to retrieve--------')