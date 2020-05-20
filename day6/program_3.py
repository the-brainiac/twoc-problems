l = list(map(int,input('Enter elements of list: ').split()))
print('List is : ',l)
l.sort()
print(l)
l1=[]
for i in range(len(l)):
	if l[i]>0:
		l1=l[i:]
		break
print(l1)
for i in range(len(l1)):
	if l1[i]!=i+1:
		print('missing number is :',i+1)
		break
