num_array = list(map(int,input('Enter number seperated by space: ').split()))
print(num_array)
size = len(num_array)
for i in range(size-1):
	num_array[i]=max(num_array[i+1:])
num_array[-1]=-1
print(num_array)
