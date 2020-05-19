from itertools import combinations

wt = list(map(int,input('enter weights:').split()))
val = list(map(int,input('enter values:').split()))
weight = int(input('Enter Max Weight: '))
dict={}
com=[]
for i in range(len(wt)):
	dict[wt[i]]=val[i]
	for j in combinations(wt,i+1):
		if sum(j)<=weight:
			com.append(j)
max_value=0
for i in com:
	temp=0
	for j in i:
		temp+=dict[j]
	if temp>max_value:
		max_value=temp
print(max_value)

