'''
How to Overload the Operators in Python?
Suppose the user has two objects which are the physical representation of a user-defined data type class.
The user has to add two objects using the "+" operator, and it gives an error.
This is because the compiler does not know how to add two objects.


So, the user has to define the function for using the operator, and that process is known as "operator overloading".
The user can overload all the existing operators by they cannot create any new operator.
Python provides some special functions, or we can say magic functions for performing operator overloading, which is automatically invoked when it is associated with that operator. Such as, when the user uses the "+" operator,
the magic function __add__ will automatically invoke in the command where the "+" operator will be defined.
'''

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

s1 = Student(50,50)
s2 = Student(75,75)

s3 = s1 + s2


'''

'''
