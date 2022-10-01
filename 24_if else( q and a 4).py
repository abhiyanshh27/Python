print("A store sells three items.")

A=50
B=20
C=30

qty1 = int(input("Enter the A Qty."))
qty2 = int(input("Enter the A Qty."))
qty3 = int(input("Enter the A Qty."))

A*=qty1
B*=qty2
C*=qty3

total = A+B+C

if (total>=200):
    x = total*8/100
    print("total is ",x)
else:
    print("total is ",total)
