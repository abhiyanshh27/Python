# kwargs (Keyword arguments) or
# **kwargs (Double star operator)
def func (**kwargs):
# Add both the parameters and return them."
    print(kwargs)
    print(type(kwargs))

func(f_num='Aman',l_name='Khan')

print("--------------------------")
def func2 (**kwargs):
# Add both the parameters and return them."
    for k,v in kwargs.items():
        print(f"{k} : {v}")

func2(f_name='Aman',l_name='Khan')

print("--------------------------")
def func3 (**kwargs):
# Add both the parameters and return them."
    for k,v in kwargs.items():
        print(f"{k} : {v}")

#dicionary unpacking
dict = {'name':'Aman', 'age':23}
func3(**dict)
