#Inner class in Python
class Student:      #outer class 
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop() #object of laptop class is created here

        
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
#this show method of student will be print student data

    class Laptop:       #inner class
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)
#this show method of laptop will be print laptop data

s1 = Student('Parnav',2)
s2 = Student('Abhiyansh',3)

#1st type
print("By 1st method:",s1.name, s1.rollno)


#2nd type
s1.show()




'''
#1st type : s1 is outer class object and lap it inner class object 
print(s1.lap.brand)

#2nd type   create object of laptop class 
lap1 = Student.Laptop() #because laptop class belongs to student class 

student also has a laptop with brand, cpu and ram configuration
laptop uses ony by student.

Remember:-
You can create object of inner class inside the outer class
OR
You can create object of inner class outside the outer class provided you use outer class name to call it.
'''
