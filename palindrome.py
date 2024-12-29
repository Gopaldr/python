Num=int(input('Enter a integer number:'))
rem=0
reverse_number=0
temp=Num
while(Num!=0):
    rem=Num%10
    reverse_number=reverse_number*10+rem
    Num=Num//10
if(temp==reverse_number):
    print(temp,"is a palindrome number")
else:
    print(temp,"is not a palindrome number")