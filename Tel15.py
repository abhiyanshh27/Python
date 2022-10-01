#Constructor in inheritance
#MRO > Method resolution Order
class A:
    def __init__(self):
        print("I am init constructor of A class.")
        
    def feature1(self):
        print("Feature 1 of class A is working!")

    def feature2(self):
        print("Feature 2 of class A is working!")



class B:
    def __init__(self):     
        print("I am init constructor of B class.")
        
    def feature1(self):
        print("Feature 1 of class B is working!")

    def feature2(self):
        print("Feature 2 of class B is working!")


class C(A,B):
    def __init__(self):
        super().__init__()
        print("I am init constructor of C class.")

a1 = C()        #left to right for init method
a1.feature1()   #same left to right for instance method
'''
Remember:-
What if we call the init method of super class, but now C has two super classes

whenever we have multiple inheritance, if will always start from left to right
which means MRO

'''
