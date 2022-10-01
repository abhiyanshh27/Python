f = open("file1.txt","r")

print(f.name)
print(f.readline(),end='')
#print(f.readline())
#readline method ek bar me ek hi line ko read kart ahi 
f.close()
