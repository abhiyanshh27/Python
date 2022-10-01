#class start
class Student:
    def __init__(self,first_name,last_name,age):
    #create instance variable & self represent an opject
     print("init method called")
     self.first_name = first_name
     self.last_name = last_name
     self.age = age
#class end

#This would create first object fo Student class
s1= Student('Aman','Khan',14)

#Accessing object's attributes using the dot operator with object
print(s1.first_name)

s2= Student('Ritu','Rajpurohit',21)
print(s2.last_name)
