from itertools import permutations

l1 = list(map(int,input('Enter elements of a list :').split()))
sum_set = set(l1)
sum_set.add(sum(l1))

for i in range(2,len(l1)):
	for j in permutations(l1,i):
		sum_set.add(sum(j))
num=1
while 1:
	if num not in sum_set:
		print('the least integer is :',num)
		break

	num+=1