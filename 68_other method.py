s1={1,2,3,4,4,5,5,5,6,7,7,7,7,8}

set5 = {'navya', 'gyan', 'rahul', 'khushi'}
#add method
set5.add('parnav')
print("Add method:",set5)

#remove method
set5.remove('gyan')
print("\nRemove method:",set5)

#discard method
set5.discard('khushi')
print("\ndiscard method:",set5)

#set5.remove('python')
set5.discard('python')
print("\ndiscard method after using remove method:",set5)

#clear method
set5.clear()
print("\nclear method:",set5)

#copy method
set6 = s1.copy()
print("\ncopy method:",set6)
