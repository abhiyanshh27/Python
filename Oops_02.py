class emploee:
    def __init__(emp_detail,fname,lname,enum):
        emp_detail.fname = fname
        emp_detail.lname = lname
        emp_detail.enum = enum

e1 = emploee('karan','sharma',1)
print(e1.fname)

e2 = emploee('ram','dev',2)
print(e2.lname)
