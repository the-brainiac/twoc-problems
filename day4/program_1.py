from collections import Counter

l1 = tuple(input('Enter elements of a tuple').split())
c = Counter(l1)
for i in set(l1):
	print('Element',i,'occured',c[i],'times in the tuple')