n=int(input("enter a number:"))
evensum=0
oddsum=0
for i in range(0,n+1):
     evensum=i+evensum
     oddsum=i+oddsum
     if(n%2==0):
          print(evensum)
     else:
          print(oddsum)         

