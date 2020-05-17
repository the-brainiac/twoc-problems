from itertools import permutations

s = input('Enter a String :')
for i in permutations(s):
	print(("".join(i)),end=' , ')