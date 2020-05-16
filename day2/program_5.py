def add_star(s):
	s2=''
	for i in s:
		s2+=i+'*'
	return s2[:-1]

n=int(input('Enter number:'))
for i in range(n,0,-1):
	print(add_star(str(i)*i))

for i in range(1,n+1):
	print(add_star(str(i)*i))
