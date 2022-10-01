#special method : __init__(self)
class Computer:
    def __init__(self):
        print("in init")
    #like constructor
    def config(self):
        print("i5, 16gb, 1TB")

com1 = Computer()
com2 = Computer()



print("2nd method : object itself to call the function")
com1.config()
com2.config()
