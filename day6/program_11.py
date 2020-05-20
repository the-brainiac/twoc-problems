l = list(map(int,input('enter list elements: ').split()))
l.sort()
product=l[-1]*l[-2]*l[-3]
print(product)
