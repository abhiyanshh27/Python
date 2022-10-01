f = open("file1.txt","r")

print(f.name)
'''
lines = f.readlines()
for line in lines:
    print(line,end='')
'''

print(f.readlines())
f.close()
