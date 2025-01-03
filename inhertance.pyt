class vehicle:
    def __init__(self):
        print("iam the vehicle class constructer...")
class bike(vehicle):
    def __init__(self):
        super().__init__()
        print("iam the bike class....")
class superbike(bike):
    def __init__(self):
         super().__init__()
         print("iam the super bike class constructer...")
s1=superbike()  
print("------------------------------------------------------------------")

#hirachail inhertance
class engineering:
    def __init__(self):
        print("iam the engineering class constructer...")
class CSE(engineering):
    def __init__(self):
        super().__init__()
        print("iam the CSE class....")
class MECH(engineering):
    def __init__(self):
         super().__init__()
         print("iam the mech class constructer...")
s2=MECH()  
s3=CSE()
s4=engineering()
print("--------------------------------------------------------------------")

#hiearchial inhertance
class sports:
    def __init__(self):
        print("iam the sports class constructer...")
class cricket(sports):
    def __init__(self):
        super().__init__()
        print("iam the sports class....")
        print("----------------------")
class kabbadi(sports):
    def __init__(self):
         super().__init__()
         print("iam the kabbadi class constructer...")
         print("-------------------------")
class kho_kho(sports):
    def __init__(self):
        super().__init__()
        print("iam the kho kho class constructer..")
s7=cricket()
s8=kabbadi()
s9=kho_kho()

#hybrid inhertance
class a:
    def __init__(self):
        print("class a")
class b(a):
    def __init__(self):
        super().__init__()
        print("it is class b")
class c(a):
    def __init__(self):
        super().__init__()
        print("class c")
class d(b,c):
    def __init__(self):
        super().__init__()
        print("class d")
c1=d()