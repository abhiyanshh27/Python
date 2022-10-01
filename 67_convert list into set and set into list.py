s1 = {5,2,3,1,4}

#printing set variable
print ("s1 = ",s1)

#data type of variable s1
print(type(s1))


s2 = {1,2,2,3,4,4,}
print("Show unique values : ",s2)

#indexing not possible
s3 = {1,2,3}
#s3[1]

#set as list and list as set
L1 = [1,2,3,4,4,5,5,5,6,7,7,7,7,8]
print(L1)

#convert list into set
s4 = set(L1)
print("List to Set : ",s4)

#convert set into list
s4 = list (set(L1))
print("Set to List : ",s4)
