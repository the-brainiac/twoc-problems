#since no input format was given i am assuming that list elements were entered in a single line seperated by a space

l = list(input('Enter elements of a list:').split())
print('original list : ',l)
print('list after removing duplicates : ',list(set(l)))