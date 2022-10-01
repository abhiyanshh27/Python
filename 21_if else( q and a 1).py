print("WNP to check that user can vote or not.")

num = int (input ("Enter your age : "))

if(num>=18):
    print("you give the vote.")
elif(num<18):
    num=18-num
    print("sorry you age is under 18.")
    print("you can wait.",num,"year")
else:
    print("type right number.")
