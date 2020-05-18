arr=[]
for _ in range(int(input('Enter number of vote: '))):
	arr.append(input('Enter name of candidates to vote: '))
new_arr=[]
for i in set(arr):
	new_arr.append([arr.count(i),i])
new_arr.sort()
votes = new_arr[-1][0]
winner_array=[]
for i in new_arr:
	if i[0]==votes:
		winner_array.append(i[1])
print('The winner is :',sorted(winner_array)[0])