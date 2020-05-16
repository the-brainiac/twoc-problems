def oddeven(num):
	if num%2==0:
		print('Number is EVEN')
	else:
		print('Number is ODD')

def check_prime(num):
	flag=0
	for i in range(2,num//2):
		if num%i==0:
			flag+=1
	if flag==0:
		print('Number is PRIME')
	else:
		print('Number is not PRIME')

def check_palindrome(n):
	s=str(n)
	if s==s[::-1]:
		print('Number is PALINDROME')
	else:
		print('Number is not PALINDROME')

def check_armstrong(n):
	s=str(n)
	num=0
	for i in s:
		num+=int(i)**3
	if n==num:
		print('Number is Armstrong')
	else:
		print('Number is not Armstrong')



n = int(input('Enter a number:'))
oddeven(n)
check_prime(n)
check_palindrome(n)
check_armstrong(n)