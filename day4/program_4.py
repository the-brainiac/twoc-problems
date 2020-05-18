d=dict()
d1=dict()
for _ in range(int(input('Enter the Number of values you want:'))):
	key = input('Enter The key : ')
	value = int(input('Enter the value: '))
	d[key]=value
	if value not in d1.values():
		d1[key]=value
print('original dictionary:',d)
print('dictionary without duplicate values:',d1)