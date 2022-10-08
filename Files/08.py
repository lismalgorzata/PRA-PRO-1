file = open('countries.txt','r')
# displaying text file, line by line
count=0
for line in file:
    count+=1
    print(count, end=" ")
    print(line, end="")
file.close()
