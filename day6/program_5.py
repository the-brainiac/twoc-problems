arr=[0,1,1,2,3,5,8,13,21,34]
a=0
b=1
while 1:
	if b<sum(arr):
		temp=b
		b=a+b
		a=temp
		if b==sum(arr):
			print('sum of fibonacci is a fibonaccinumber')
			break
		if b>sum(arr):
			print('sum of fibonacci is not a fibonaccinumber')
			break