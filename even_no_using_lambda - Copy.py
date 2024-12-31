num=int(input("Enter a number:"))
value=lambda num:print("even") if (num%2==0) else print("not even")
value(num)


#number or digit of given integer using lambda
num=int(input("Enter a number:"))
value=lambda num:print("digit") if (num>=-9 and num<=9) else print("number")
value(num)

#finding two digit or three digit number using lambda
num=int(input("enter an integer :"))
value=lambda num:print("it is a two digit number") if (num>=-99 and num<=99) else print("it is not a two  digit number") 
value(num)