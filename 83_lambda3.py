'''
without lambda function
def check_len(s):
    if len(s) > 5:
        return True
    else:
        return False
or
def check_len(s):
    return len(s) > 5:
print(check_len('Python'))
'''
#lambda practice 2 with if_else
check_len2 = lambda s : True if len(s)>5 else False
print(check_len2('Python'))
'''
or
check_len2 = lambda s : len(s)>5
print(check_len2('Python'))
'''
