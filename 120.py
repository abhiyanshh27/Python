class student:
    def __init__(std_detail,first_name,last_name,age):
        print("init method called")
        std_detail.first_name = first_name
        std_detail.last_name = last_name
        std_detail.age = age

s1= student('Aman','Khan',14)
print(s1.first_name)

s2= student('Ritu','Rajpurohit',21)
print(s2.last_name)
