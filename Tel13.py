'''
How constructor behaves in inheritance?
How to use super() method in inheritance?
What is MRO?
'''
class A:
    def __init__(self):
        print("I am init constructor of A class.")
        
    def feature1(self):
        print("Feature 1 of class A is working!")

    def feature2(self):
        print("Feature 2 of class A is working!")



class B(A):
    def __init__(self):
        print("I am init constructor of B class.")
        
    def feature1(self):
        print("Feature 1 of class B is working!")

    def feature2(self):
        print("Feature 2 of class B is working!")

#a1 = A()
a1 = B()

'''
Remember:-
Sub class (B) can access all the features of Super class (A)
But
Super class (A) can not access any features of Sub class (B)

If you create object of Sub class (B) it will first try to find init of Sub Class (B)
If it is not found then it will call init of Super class (A)
'''
