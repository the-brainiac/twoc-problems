d=[]
for _ in range(int(input('Enter number of words: '))):
	d.append(input('Enter word: '))
char = input('Enter character set seperated by a space: ').split()
array=[]
for word in d:
	if set(word).issubset(set(char)):
		array.append(word)
print(", ".join(array),end='.')
