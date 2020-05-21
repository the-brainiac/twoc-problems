s=input('Enter a number: ')
num=[int(i) for i in s]
for i in range(len(num)-1,0,-1):
	if num[i]>num[i-1]:
		num[i-1],num[-1]=num[-1],num[i-1]
		num1=num[:i]+sorted(num[i:])
print(num1)