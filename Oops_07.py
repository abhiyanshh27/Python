class person:
    full_name = "Abhiyansh Vaishnav"
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = person('Parnav','Bhati',19)
p2 = person('Abhiyansh','Vaishnav',18)

print(person.full_name)
