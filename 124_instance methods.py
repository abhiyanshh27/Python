#instance methods
class person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name}{self.last_name}"

p1 = person('Parnav','Bhati',24)
p2 = person('Abhi','Vaishnav',24)

#print(p2.full_name())
person.full_name(p2)
