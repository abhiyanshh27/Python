'''

def add (arg1, arg2):
# Add both the parameters and return them."
    total = arg1 + arg2
    pritn("Inside the function : ", total)
    return total

#Now you can call add function
total = add (10, 20, 30, 40)
#what if i pass more arg
print ("Outside the function :", total )

'''
def all_add ( *args ):
# Add both the parameters and return them."
    print(args)
    print(type(args))
all_add(10, 20, 30, 40)

def all_add2 ( *args ):
# Add both the parameters and return them."
    total = 0
    for num in args:
        total+=num 
    return total

print("Total of all args:",all_add2(10, 20, 30, 40))
