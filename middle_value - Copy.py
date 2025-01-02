a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if((a<b and a>c) or (a>b and a<c)):
    print(a,"is the middle value...")
elif((b<a and b>c)or(b>a and b<c)):
    print(b,"is the middle value...")
else:
    print(c," is the middle value...")
    