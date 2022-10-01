'''
How to Overload the Operators in Python?
'''

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __gt__(self,other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1>r2:
            return True
        else:
            return False

        
        
s1 = Student(50,50)
s2 = Student(75,75)

#s3 = s1 + s2        # behind the scence -> Student.__gt__(s1-> self,s2->other)

#print(s3.m1)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

'''

'''
