print("Calulate the gross salary of an employee in particular company.")

num = int(input("Enter the basic salary."))

if (num>=2000):
    HRA = 500
    DA = num/2
    print("value of HRA",HRA)
    print("value of DA",DA)
else:
    HRA = num*10/100
    DA = num*25/100
    print("value of HRA",HRA)
    print("value of DA",DA)
