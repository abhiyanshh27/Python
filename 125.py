#class start
class student:
    def __init__(std_detail,first_name,last_name,age):
        #create instance variable & self > std_detail (type anyting)
        print("init method called")
        std_detail.first_name = first_name
        std_detail.last_name = last_name
        std_detail.age = age

    def displaystd(self):
        print("First_name : ", self.first_name, "last _name : ",self.last_name,"age : ",self.age)

#class end
#This would create first object of student class
s1 = student('Ritu','Rajpurohit',21)
s2 = student('Ritu','Khan',22)

#Accessing object's attributes using the dot operator with object & instance method
s1.displaystd()
s2.displaystd()
