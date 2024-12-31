num=int(input("enter a number :"))
result =list(map(lambda i:print(i),range(1,num+1)))

#n numbers of even numbers
result1=list(map(lambda i:print(i) if (i%2==0) else print(""),range(1,num+1) ))

# n numbers of even number
result2=(int(input("enter the value:")))
list(map(lambda i:print(i),range(2,result2+1,2)))
#n numbers of odd numbers
result3=(int(input("enter the value:")))
list(map(lambda i:print(i),range(1,result3+1,2)))