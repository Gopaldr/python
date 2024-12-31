def mul(n):
    for i in range(1,11):
        print(n,"x",i,"=",(n*i))
    print("-----------------------------------")
mul(4)
mul(254)


#addition
def add(n):
    for i in range(5,40,5):
        i+=1
        print(i)
add(10)

#multiplication of tables
def muli(n):
    for i in range(n):
        for j in range (1,11):
            print(i,"x",j,"=",(i*j))
muli(12)
muli(34)