#Inheritance (concept of parent/super and child/sub class)
class A:
    def feature1(self):
        print("Feature 1 of class A is working!");

    def feature2(self):
        print("Feature 2 of class A is working!");



class B:
    def feature3(self):
        print("Feature 3 of class B is working!");

    def feature4(self):
        print("Feature 4 of class B is working!");

#By A class 
a1 = A()
a1.feature1()
a1.feature2()


#By B Class
b1 = B()
b1.feature3()
b1.feature4()
