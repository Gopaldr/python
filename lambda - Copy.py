#declaring the lambda function
res=lambda age:print(age)
res(12)

#multiplication using lambda 
mul=lambda a,b:print(a*b)
mul(3,8)

#returnig multiple values 
avg=lambda a,b: (a+b,a-b,a*b)
add,sub,mull=avg(10,5)
print(add)
print(sub)
print(mull)