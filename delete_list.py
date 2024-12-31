prog_language=["c","c++","python","java","html","css","javascript"]
print(prog_language)
print(type(prog_language))
print("------------------------------------------")
del prog_language[6]
print(prog_language)
print("---------------------------------------------")
del prog_language[3]
print(prog_language)
del prog_language[0:5]
print(prog_language)

# without using index values
for i in prog_language:
    print(i)

#using index iteration
for i in  range (len(prog_language)):
    print(prog_language)

