f = open("sample1.txt", "r")
copy = open("copylines.txt", "w")
for line in f:
    copy.write(line)
f.close()
copy.close()

copy=open('copy.txt')
print(copy.read())