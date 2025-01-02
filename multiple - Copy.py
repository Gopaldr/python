Mul=int(input("enter a number:"))
if(Mul%3==0 and Mul%5==0):
    print(Mul,"is a multiple of both 3 and 5:")
else:
    print(Mul,"is not a multiple:")

# terinal operator is used
value="it is  a multiple "if(Mul%3==0 and Mul%5==0) else "is not a multiple"
print(value)