class MarketPen:
    def __init__(self,color,price,brand):
        self.color=color
        self.price=price
        self.brand=brand
    #Mutator Methods
    def set_color(self):
        self.color='Red'
    def set_price(self):
        self.price=25
    def set_brand(self):
        self.brand='Doms'
    #Accessor Method:
    def show_color(self):
        return self.color
    def show_price(self):
        return self.price
    def show_brand(self):
        return self.brand
m1=MarketPen('black',20,'camelin')
res1=m1.show_color()
print(res1)
res2=m1.show_brand()
print(res2)
res3=m1.show_price()
print(res3)
print("------------------------------")
m1.set_color()
m1.set_price()
m1.set_brand()
res1=m1.show_color()
print(res1)
res2=m1.show_brand()
print(res2)
res3=m1.show_price()
print(res3)