file=open('integers1-50.txt','w')
for i in range(1,51):
    number=str(i)
    file.write(number)
    file.write('\n')
file.close()

file=open('integers1-50.txt','r')
print(file.read())