print("calculate the telephone bill of a customer.")

num = int(input ("Enter the number of calls :"))

if(num<=100):
    num*=.80
    print("total cost of calls",num)
elif(num<100 and num>=200):
    num*=1.0
    print("total cost of calls",num)
elif(num>200):
    num*=1.20
    print("total cost of calls",num)
              
