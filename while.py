Num=int(input("Enter a number:"))
evendigitcount=0
rem=0
while (Num!=0):
    rem=Num%10
    if(rem%2==0):
        evendigitcount+=1
        Num=Num//10
print("Number of even digits are",evendigitcount)
    

#odd numbers
Num=int(input("Enter a number:"))
odddigitcount=0
rem=0
while (Num!=0):
    rem=Num%10
    if(rem%2!=0):
        odddigitcount+=1
        Num=Num//10
print("Number of odd digits are",odddigitcount)
    