a=[1,3,4,6,7]
b=[5,8,4,4,85]
print(a)
print(b)
a.extend(b)
print(a)
b.extend(a)
print(b)

#count method
count=b.count(4)
print(count)