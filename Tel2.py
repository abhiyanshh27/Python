class Computer:
    def config(self):
        print("i5, 16gb, 1TB")

com1 = Computer()
com2 = Computer()

print("1st method : class call the funtion and pass object as a argument")
Computer.config(com1)
Computer.config(com2)

print("2nd method : object itself to call the function")
com1.config()
com2.config()
