num_array = list(map(int,input('Enter number seperated by space: ').split()))
print(num_array)
odd_array=[]
even_array=[]
for i in num_array:
	if i%2==0:
		even_array.append(i)
	else:
		odd_array.append(i)
print(sorted(odd_array,reverse=True)+sorted(even_array))