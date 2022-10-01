#in keyword in sets and for loop

s = {'a', 'b', 'c'}
#in keyword to check if item is present or not in set
if 'a' in s:
    print("Present")
else:
    print("Not Present")



#in keyword with set and loop
for item in s:
    print(item)

#union and intersection in set
s1 = {1,2,3,4}
s2 = {3,4,5,6}

union_set = s1 | s2
print("Remove duplicate item after union:",union_set)

insec_set = s1 & s2
print("Remove unique item after intersection:",insec_set)
