class Student:
    def __init__(std_detail,first_name,last_name,age):
        print("init method called")
        std_detail.first_name = first_name
        std_detail.last_name = last_name
        std_detail.age = age

    def displayStd(self):
        print("First_name :", self.first_name,"Last_name :", self.last_name,"Age :", self.age)

s1 = Student('Aman','Khan',14)
s2 = Student('Ritu','Rahpurohit',21)

s1.displayStd()
s2.displayStd()
