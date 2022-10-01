class employee:
    def __init__(emp_detail,fname,lname,enum):
        emp_detail.fname = fname
        emp_detail.lname = lname
        emp_detail.enum = enum

    def displayemp(self):
        print("First_name :",self.fname,"Last_name :",self.lname,"emp._number :",self.enum)

e1=employee('karan','sharma',1)
e2=employee('ram','dev',3)

e1.displayemp()
e2.displayemp()
