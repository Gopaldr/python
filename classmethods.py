class student:
    @staticmethod
    def collegename():
        print(" ABC college...")
    @classmethod
    def writeexams(self):
        print("enjoy ur exams....")
    #accessor methods
    def show_name(self):
        return self.studentname
    #mutator method
    def set_name(self):
        self.studentname="scott"
    def __init__(self,studentname,id,email):
        print("object is created....")
        self.studentname=studentname
        self.id=id
        self.email=email
student.collegename()
student.writeexams()
stu=student("sai",25,"sai@gmail") 
stu.collegename()
stu.set_name()
stu.set_name()      
