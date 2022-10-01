class Student:      #outer class 
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
        
    def show(self):
        print(self.name, self.rollno)

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

    
s1 = Student('Parnav',2)
s2 = Student('Abhiyansh',3)

#1st type
print("By 1st method:",s1.name, s1.rollno)

print(s1.lap.brand)


#2nd type
s1.show()
