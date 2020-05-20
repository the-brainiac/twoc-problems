from itertools import combinations

array = list(map(float,input('Enter all numbers : ').split()))
com = combinations(array,3)
l=[]
for a,b,c in com:
	if a+b+c>1 and a+b+c<2:
		l.append((a,b,c))
print(l)