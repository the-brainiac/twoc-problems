n=int(input('Enter number:'))
for i in range(n):
	s=' '*i+'*'+' '*(n-i-1)
	print(s+s[::-1])
for i in range(n):
	s=' '*(n-i-1)+'*'+' '*i
	print(s+s[::-1])
