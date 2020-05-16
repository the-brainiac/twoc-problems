n=int(input('Enter number:'))
for i in range(n):
	s='* '*(n-i)+'  '*i
	print(s+s[::-1])

for i in range(1,n+1):
	s='* '*i+'  '*(n-i)
	print(s+s[::-1])
