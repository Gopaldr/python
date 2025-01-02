Num=int(input("Enter a number:"))
for i in range(1,11):
    print(Num,"x",i,"=",i*Num)

#multiplcation tables from 1 to n
Num=int(input("Enter a number:"))
for i in range(1,11):
    print(Num,"x",i,"=",Num*i)
    for j in range(1,Num+1):
        print(Num,"x",j,"=",Num*j)