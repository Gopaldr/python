class duck:
    def walk(self):
        print("thapak thapka thapak thapak")
class horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak")
def myfunction(obj):
    obj.walk()
d=duck()
myfunction(d)
h=horse()
myfunction(h)

#
class father:
    def work(self):
        print("Hard working father...!")
class son:
    def work(self):
        print("Enjoying son...!")
def result(self):
    self.work()
f1=father()
result(f1)
s1=son()
result(s1)

#Strong Typing
class duck:
    def walk(self):
        print("thapak thapka thapak thapak")
class horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak")
class cat:
    def talk(self):
        print("Meow Meow")
def myfunction(obj):
    if hasattr(obj, 'walk'):
        obj.walk()
    if hasattr(obj, 'talk'):
        obj.talk()
d=duck()
myfunction(d)
h=horse()
myfunction(h)
c=cat()
myfunction(c)

#
class engineer:
    def work(self):
        print("Engineer is working...!")
class softwareengineer(engineer):
    def work(self):
        print("Software Engineer is working.....!")
class electricalengineer(engineer):
    def work(slef):
        print("Electrical Engineer is working...!")
e1=engineer()
e1.work()
se1=softwareengineer()
se1.work()
ee1=electricalengineer()
ee1.work()