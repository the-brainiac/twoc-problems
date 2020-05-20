l = list(map(int,input('Enter list elements:').split()))
k = int(input('Enter value of k:'))
print(l)
print(f'{k}th smallest in the list is {sorted(l)[k-1]}')