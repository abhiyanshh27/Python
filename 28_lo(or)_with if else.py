print("WAP to use OR Logical operator.")
print("When both conditions are true.")
a=7
b=5
c=3
if(a>b or b>c):
    print("True")
else:
    print("False")

print("When one of condition are false.")
if(a>b or b<c):
    print("True")
else:
    print("False")

print("When both vonditions are false.")
if(a<b or b<c):
    print("True")
else:
    print("False")
