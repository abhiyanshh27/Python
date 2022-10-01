class employee:
    def __init__(emp_detail,fname,lname,enum):
        emp_detail.fname = fname
        emp_detail.lname = lname
        emp_detail.enum = enum
        
e1=employee('karan','sharma',1)
e2=employee('ram','dev',3)

print(e1.fname)
print(e2.lname)

print(hasattr(e1,'enum'))
print(getattr(e1,'enum'))

setattr(e1,'salary',2500)
print(e1.salary)

print(delattr(e1,'salary'))
