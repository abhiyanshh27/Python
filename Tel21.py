'''
What is Operator Overloading in Python?
The operator overloading in Python means provide extended meaning beyond their predefined operational meaning.
Such as, we use the "+" operator for adding two integers as well as joining two strings or merging two lists.
We can achieve this as the "+" operator is overloaded by the "int" class and "str" class.
The user can notice that the same inbuilt operator or function is showing different behaviour for objects of
different classes. This process is known as operator overloading.
'''

print (14 + 7)  
   
# Now, we will concatenate the two strings  
print ("Python" + "Class")  
   
# We will check the product of two numbers  
print (2 * 4)  
   
# Here, we will try to repeat the String  
print ("Python " * 3)  

'''
a = 5
b = 'World'
print(a+b)
'''

'''
a = 5
b = 6
print(a + b)

#behind the scence
print(int.__add__(a,b))     # add method belongs to int class
'''

'''
a = '5'
b = '6'
print(a + b)
#behind the scence
print(str.__add__(a,b))     # add method belongs to str class
'''

'''
Operator    method
+           __add__()
-           __sub__()
*           __mul__()
/           __div__()
'''







