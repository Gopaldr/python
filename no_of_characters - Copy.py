str=input("Enter a string:")
count1=0
count2=0
count3=0
for i in str:
    if(i.isalpha()):
        count1+=1
    elif(i.isdigit()):
        count2+=1
    else:
        count3+=1
print("no of alphabets:",count1)
print("no of digits:",count2)
print("no of special characters:",count3)