class Employee():
    def __init__(self,name,id,designation,salary,location,special_allowances):
        print("Employee Infomation :")
        self.name=name
        self.id=id
        self.designation=designation
        self.salary=salary
        self.location=location
        self.special_allowances=special_allowances
emp1=Employee("Gopal",503,"CEO",100000,"guntur","Wifi allowances")
print("Employee name:",emp1.name)
print("Employee Id :",emp1.id)
print("Employee Designation",emp1.designation)
print("Employee Salary :",emp1.salary)
print("Employee Location :",emp1.location)
print("Employee Special_Allowance :",emp1.special_allowances)

#direct intialization
class Student2:
    def __init__(self):
        print("student info :")
        self.stu_name="sai"
        self.stu_id=501
        self.stu_age=20
        self.stu_branch="Cse"
stu1=Student2()
print("Student Name :",stu1.stu_name)
print("Student Id :",stu1.stu_id)
print("Student Age :",stu1.stu_age)
print("Student Branch :",stu1.stu_branch)
