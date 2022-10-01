#Inheritance (concept of parent/super and child/sub class)
#Multi Level Inheritance
class A:
    def feature1(self):
        print("Feature 1 of class A is working!");

    def feature2(self):
        print("Feature 2 of class A is working!");



class B(A):         #child class of A 
    def feature3(self):
        print("Feature 3 of class B is working!");

    def feature4(self):
        print("Feature 4 of class B is working!");



class C(B):         #child class of B
    def feature5(self):
        print("Feature 5 of class C is working!");

    def feature6(self):
        print("Feature 6 of class C is working!");

        
#By C Class
print("\nFeatures of Class A & B inherit by Class C")
c1 = C()
c1.feature5()
c1.feature6()

c1.feature1()
c1.feature2()

c1.feature3()
c1.feature4()
