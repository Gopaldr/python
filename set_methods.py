a=set()#prints empty set
a={19,20}
print(a)
print(id(a))#id of the given set

a.add(19.20)#adding a single element to the set
print(a)
a.update([10,20,304])#adding more than one elements in a set
print(a)
a.discard(10) 
a.remove(20)
print(a)

#additional set methods
b={'hi','hello','how are you',19}
c=a.intersection(b)#same elements in both the sets
print(c)
c=a.union(b)#print all the elements in the set
print(c)
c=a.difference(b)#print a elements that are unique or that is only exist in one set not in both the sets
print(c)
c=a.issubset(b)#it returns true if all items in the set exists in the specific set
print(c)
c=a.issuperset(b)#it returns true if all items in the set exist in the original set
print(c)