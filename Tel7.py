#Inner class in Python
class Student:
    def __init__(self,name,rollno,brand,cpu,ram):
        self.name = name
        self.rollno = rollno

        self.brand = brand
        self.pro = cpu
        self.ram = ram
        
    def show(self):
        print(self.name, self.rollno)
s1 = Student('Parnav',2,'HP','i5',8)
s2 = Student('Abhiyansh',3,'Dell','i3',16)

#1st type
print("By 1st method:",s1.name, s1.rollno, s1.brand, s1.pro, s1.ram)


#2nd type
#s1.show()
