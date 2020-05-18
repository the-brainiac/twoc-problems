d=dict()
for _ in range(int(input('Enter the Number of values you want:'))):
	key = input('Enter The key : ')
	d[key] = int(input('Enter the value: '))
l=list(d.values())
for i in (sorted(l))[::-1]:
	if i<max(l):
		print('Second highest value is ',i)
		break