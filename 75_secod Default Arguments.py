def student_info(f_name,l_name,age):
    print(f"Your first name is {f_name}")
    print(f"Your last name is {l_name}")
    print(f"Your age is {age}")

student_info('Aman','Khan',14)
'''
def student_info1(f_name,l_name,age):
    print(f"Your first name is {f_name}")
    print(f"Your last name is {l_name}")
    print(f"Your age is {age}")

student_info1('Aman','Khan')
TypeError: student_infol() missing 1 required
positional argument: 'age'
'''

#Default parameters
def student_info2(f_name,l_name,age=23):
    print(f"\nYour first name is {f_name}")
    print(f"Your last name is {l_name}")
    print(f"Your age is {age}")

student_info2('Seema','Rajpurohit')

