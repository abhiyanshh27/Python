class employee:
    def __init__(emp_detail,fname,lname,enum):
        emp_detail.fname = fname
        emp_detail.lname = lname
        emp_detail.enum = enum

e1=employee('karan','sharma',1)
e2=employee('ram','dev',3)

print(e1.fname)
print(e2.lname)

e1.fname="Joya"
print(e1.fname)

e1.salary=2500
print(e1.salary)

del e1.salary
print(e1.salary)
