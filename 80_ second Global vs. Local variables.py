num = 7         # This is global variable.

# Function defintion is here
def func():
    num = 5         #This is local variable.
    return num
# Now you can call func function
print("Inside the function local variable : ",func())
print("Outside the function global variable : ",num)
