print("WAP to show the use of nested while loop.")
i = 1
j = 1
while (i<=5):
    print("Scope")
    while (j<=4):
        print("Jodhpur")
        j=j+1
    i+=1

print ("\nOutput=ScopeJodhpurJodhpurJodhpurJodhpur")
i = 1
while(i<=5):
    print("scope",end="")
    j = 1
    while (j<=4):
        print("Jodhpur",end="")
        j+=1
    i+=1
    print()
