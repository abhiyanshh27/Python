f = open("file1.txt","r")

print(f.tell())
print(f.read())

print(f.tell())

f.seek(0)
print(f.tell())
print(f.read())

f.close()
