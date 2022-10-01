#Types of variable : 
class Car:
    wheels = 4
    def __init__(self):
        self.com = "BMW"
        self.mil = 10
        
c1 = Car()
c2 = Car()

#update value of instance variable
#c1.mil = 8

#update value of class variable 
#Car.wheels = 5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)

'''
if you define a variable inside init its called instance variable
if you define a variable outside init its called class (static) variable
wheels is common to all the objects > class variable

what is namespace ?
namespace is an area or place where you create and store object/variable
two types of namesapce
    class namespace > wheels are belong to class 
    object or instance namespace > com and mil are belongs to object










    
'''
