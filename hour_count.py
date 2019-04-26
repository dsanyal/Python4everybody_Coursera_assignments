import re
handle = open('mbox-short.txt')

count = dict()
regex = re.compile('\d{2}:\d{2}:\d{2}')
c=0
for line in handle:
	if  len(line.split())>0 and line.split()[0]=='From':
		time=regex.search(line)
		if time:
			hour = time.group().split(':')[0]
			count[hour]=count.get(hour,0)+1
handle.close()		
#tmp = sorted([(v,k) for k,v in count.items()], reverse=True)
#for tup in tmp:
#	print (tup[::-1])
hour_sorted = sorted(count.items())
for tup in hour_sorted:
	print(tup[0],tup[1])