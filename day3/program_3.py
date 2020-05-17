s = input('Enter a String :')
new_s=''
for i in s:
	if i not in new_s:
		new_s+=i
print(new_s)