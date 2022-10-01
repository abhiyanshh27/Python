#Constructor in inheritance
#MRO > Method resolution Order
class A:
    def __init__(self):
        print("I am init constructor of A class.")
        
    def feature1(self):
        print("Feature 1 of class A is working!")

    def feature2(self):
        print("Feature 2 of class A is working!")



class B(A):
    def __init__(self):
        super().__init__()      
        print("I am init constructor of B class.")
        
    def feature1(self):
        print("Feature 1 of class B is working!")

    def feature2(self):
        print("Feature 2 of class B is working!")


a1 = B()

'''
Remember:-
Sub class (B) can access all the features of Super class (A)
But
Super class (A) can not access any features of Sub class (B)

If you create object of Sub class (B) it will first try to find init of Sub Class (B)
If it is not found then it will call init of Super class (A)
If you have call super then it will first call init of Super class then call init of Sub class

what if we call the constructor of Super class A
super() is a special method to call all features of super class 
'''
