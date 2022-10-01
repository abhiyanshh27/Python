#Types of method 
class Student:
    school = 'Scope'
    def __init__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod    
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is student class...in Moduel3.")


s1 = Student(50,50,50)
s2 = Student(75,75,75)

print(s1.avg())
print(Student.getSchool())  #if we do not write decorator then display error for this line
Student.info()

'''
instance variable can be used with instance method or work with instance method
if we work with instance method then we can pass 'self keyword' as a argument

class variable can be used with class method or work with class method
if we work with class method then we can pass 'cls (class) keyword' as a argument

static method
a method which has nothing to do with the instance method and class method
if we want to do something different 
'''










