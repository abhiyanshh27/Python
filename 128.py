class laptop:
    def __init__(self, brand_name, model_name, price):
        #instance variables
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def apply_discount(self,num):
        #self.prince
        off_price = (num/100)*self.price
        dis = self.price - off_price
        return dis

laptop1 = laptop('hp','aull4x',10000)
laptop2 = laptop('apple','mackbook pro',100000)

print(laptop1.brand_name)
print(laptop2.model_name)

print(laptop1.apply_discount(1))
