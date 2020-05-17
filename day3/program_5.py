l1 = list(input('Enter elements of a list 1:').split())
l2 = list(input('Enter elements of a list 2:').split())

print('List 1: ',l1)
print('List 2: ',l2)
print('Intersection : ',list(set(l1).intersection(set(l2))))