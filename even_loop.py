Num=int(input("Enter a number:"))
print("even numbersfrom 1 to n:",Num)
for i in range(0,Num+1):
    if(i%2==0):
        print(i)

#by using stepsize method
Num=int(input("Enter a number:"))
for i in range(0,Num+1,2):
    print(i)