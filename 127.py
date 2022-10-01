#class start
class student:
    std_count=0
    def __init__(self,first_name,last_name,age):
        #create instance variable & self > std_detail (type anyting)
        print("init method called")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        #Student.std_count += 1   this statement increament counting one by one

    def displaystd(self):
        print("First_name : ",self.first_name,",Last_name : ",self.last_name,",Age : ",self.age)

    def difplaycount(self):
        student.std_count

#class end
#This would create first object of student class
s1 = student('Aman','Khan',14)
s2 = student('Ritu','Rajpurohit',21)

#Accenssing object's attributes using the dot operator with object & instance method
s1.displaystd()
s2.displaystd()
print("Total student : ",student.std_count)
