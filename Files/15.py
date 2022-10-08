filename=input('File name: ')

file = open(filename,'r')
# displaying text file, line by line
count=0
for line in file:
    count+=1
print('Number of lines: ',count, end=" ")
file.close()