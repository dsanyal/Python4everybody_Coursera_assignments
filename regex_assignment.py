import re


f = open('regex_data.txt')
count = 0
sum_total = 0

for line in f:
	numbers = re.findall('[0-9]+', line)
	count = count + len(numbers)
	sum_total = sum_total + sum([float(number) for number in numbers])
print('count = ',count)
print(sum_total)



'''
for line in f:
	if regex:
		numbers = regex.findall(line)
		count = count + len(numbers)
		sum_total = sum_total + sum([float(number) for number in numbers])
print('count = ',count)
print(sum_total)
'''