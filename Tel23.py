'''
How to Overload the Operators in Python?
'''

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

s1 = Student(50,50)
s2 = Student(75,75)

s3 = s1 + s2        # behind the scence -> Student.__add__(s1-> self,s2->other)

print(s3.m1)

'''

'''
