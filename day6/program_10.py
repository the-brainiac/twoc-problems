l=[]
for i in range(int(input('Enter value of K:'))):
	l1 = list(map(int,input(f'Enter values for list {i+1}: ').split()))
	l+=l1
l.sort()
print('final list is :',l)