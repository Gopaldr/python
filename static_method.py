class watch:
    @staticmethod
    def showtime():
        print("watch shows time..........")
    @classmethod
    def showbrand(self):
        print("watch brand is rolex........")
    def __init__(self,colour):
        print("object is created....")
        self.colour=colour
    def get_colour(self):
        print(self.colour)
w1=watch("silver")
watch.showtime()
watch.showbrand()
w1.get_colour()
w1.showbrand()
w1.showtime()