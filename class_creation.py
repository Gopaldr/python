class student:
    def __init__(self):
        print("object is created")
        #direct intialization
        self.name="Gopal"
        self.age=19
std1=student()
print("Student Name:",std1.name)
print("Student Age:",std1.age)
print("-------------------------")
std2=student()
print("Student Name:",std2.name)
print("Student Age:",std2.age)
print("---------------------------------------")

#New Class assing
class student1:
    def __init__(self,name,age):
        print("object is created")
        #direct intialization
        self.name=name
        self.age=age
std1=student1("Gopal Reddy",18)
print("Student Name:",std1.name)
print("Student Age:",std1.age)
print("-------------------------")
std2=student1("Murali",20)
print("Student Name:",std2.name)
print("Student Age:",std2.age)
