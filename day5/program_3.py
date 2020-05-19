house_values = list(map(int,input('Enter house values seperated by space: ').split()))
print(house_values)
size = len(house_values)
i=0
max_value=0
while i<size:
	max_value+=house_values[i]
	i+=2
print(max_value)