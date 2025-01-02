name="ramu is a good boy "
name2="ramu is a bad boy"
print(name)
print(type(name))
print("iteration through a string")
for i in name:
    print(i,end=' ')
print(name[0])

#length of a string
print(len(name))

#string sliccing
print(name[0:11])
print(name[::2])
print(name[1::2])

#string cocatination
print(name+ name2)