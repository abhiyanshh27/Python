'''
without lambda function
def is_even(a):
    if a%2 ==0:
        return True
    else:
        return False
or
def is_wven (a):
    return a%2 =0
print(is_even(7))

'''
#lambda practice 1
is_even2 = lambda a : a%2==0
print("Even :",is_even2(7))
