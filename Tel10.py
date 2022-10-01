#Inheritance (concept of parent/super and child/sub class)
#Single Level Inheritance
class A:
    def feature1(self):
        print("Feature 1 of class A is working!");

    def feature2(self):
        print("Feature 2 of class A is working!");



class B(A):         #child class
    def feature3(self):
        print("Feature 3 of class B is working!");

    def feature4(self):
        print("Feature 4 of class B is working!");

#By A class

a1 = A()
a1.feature1()
a1.feature2()
#a1.feature3()
#a1.feature4()

#By B Class
print("\nFeatures of Class A inherit by Class B")
b1 = B()
b1.feature3()
b1.feature4()

b1.feature1()
b1.feature2()







