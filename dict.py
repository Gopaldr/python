dict={1:'apple',2:'orange',3:'bannana',4:'pine apple'}
print(dict)
print(type(dict))
print(id(dict))
print(dict[1])
print(dict[2])
print(dict[3])
print(dict[4])
print(dict)
dict[5]='water mealon'
print(dict)
dict[2]='guava'
print(dict)
del dict[5]
print(dict)
del dict
print(dict)

#copying the dict
dict1={2:'hi',3:'hello'}
print(dict1)
dict2=dict1.copy()
print(dict2)
#from keys 
dict2.fromkeys('fruits','orange')
print(dict2) 

