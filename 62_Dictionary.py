L1 = [1,2,3,4,5]
L2 = ['Aman', 'Joya', 'Ram', 'Hanuman', 'John']
print("L1=",L1)
print("L2=",L2)

D1 = {'L1':[1,2,3,4,5], 'L2':['Aman', 'Joya', 'Ram', 'Hanuman', 'John']}
print("List as dictionary =",D1)

#Accessing Values in Dictionary
dict = {'Name': 'Aman', 'Class': 8, 'Percent': 84.75}
print ("\ndict['Name']: ", dict['Name'])
print ("dict['Class']: ", dict['Class'])


#Updating Dictionary
dict['Percent'] = 92.75; # update existing entry
dict['School'] = "DPS School" # Add new entry
print ("\ndict['Percent']: ", dict['Percent'])
print ("dict['School']: ", dict['School'])
print("dictionary after update=",dict)

#Delete Dictionary Elements
dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("\nBefore delete=",dict1)
del dict1['Name']    # remove entry with key 'Name'
print("After delete=",dict1)
dict1.clear()        # remove all entries in dict
print("After clear=",dict1)
#del dict1             delete entire dictionary


#Properties of Dictionary Keys
#(a)
dict2 = {'Name': 'Zara', 'Age': 7, 'Name': 'Python'}
print ("\ndict2['Name']: ", dict2['Name'])

'''
#(b)
dict3 = {['Name']: 'Zara', 'Age': 7}
print ("dict3['Name']: ", dict3['Name'])
'''
#Built-in Dictionary Functions & Methods
print ("\nLength :" , len (D1))
print ("Variable Type :", type (D1))



