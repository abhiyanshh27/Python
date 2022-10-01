class Student:
    def __init__(std_detail,first_name,last_name,age):
        std_detail.first_name = first_name
        std_detail.last_name = last_name
        std_detail.age = age

s1 = Student('Aman','Khan',14)
print(s1.first_name)

s2 = Student("Ritu","Rajpurohit",21)
print(s2.last_name)

print(hasattr(s1,'age'))

print(getattr(s1,'age'))

setattr(s1,'percentage',84.75)
print(s1.percentage)

print(delattr(s1,'percentage'))
