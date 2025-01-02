str=input("enter a string:")
count=0
for i in str:
    if(i in ('a','e','i','o','u','A','E','I','O','U')):
        count+=1
print(" vowel count:",count)


#vowels and consents
str=input("enter a string:")
str=str.lower()
str=str.replace(' ','')
count=0
consets=0
for i in str:
    if(i in ('a','e','i','o','u','A','E','I','O','U')):
        count+=1
    elif(i.isalpha()):
          consets+=1
print("vowel count:",count)
print("consents count:",consets)