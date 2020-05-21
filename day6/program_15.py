
l=list(map(int,input('Enter List elements: ').split()))
print(l)
flag =0
for i in range(1,len(l)-2):
	m1=max(l[:i])
	m2=min(l[i+1:])
	if l[i]>m1 and l[i]<m2:
		print(f'element is {l[i]} at index {i}')
		flag+=1
if flag==0:
	print('No such element exist')