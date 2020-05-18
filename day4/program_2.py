l=[]
for _ in range(int(input('enter number of elements in a list:'))):
	l.append(tuple(input('Enter tuple elements').split()))
n=int(input('Enter index value to sort the list:'))
print(l)
print(sorted(l[n-1:])+sorted(l[:n-1]))