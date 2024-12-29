student=(input("Enter student name:"))
subject1=int(input("enter maths marks:"))
subject2=int(input("enter social marks:"))
subject3=int(input("enter eng marks:"))
total=subject1+subject2+subject3
avg=total/3
print("total:",total)
print("avg:",avg)

if(avg>90):
    print("congratulation you got the first class")
elif(avg>75):
    print("congratulation you got the second class")
elif(avg>60):
    print("congratulation you got the third class")
else:
    print("fail")

#student report
student=(input("Enter student name:"))
subject1=int(input("enter maths marks:"))
subject2=int(input("enter social marks:"))
subject3=int(input("enter eng marks:"))
total=0
avg=0
print("subject1=",subject1)
print("subject2=",subject2)
print("subject3=",subject3)
if(subject1>=35 and subject2>=35 and subject3>=35):
    total=subject1+subject2+subject3
    print("total:",total)
    avg=total/3
    print("avg=",avg)
    if(avg>90):
      print("congratulation you got the first class")
    elif(avg>75):
      print("congratulation you got the second class")
    elif(avg>60):
      print("congratulation you got the third class")
   
else:
    print("fail")