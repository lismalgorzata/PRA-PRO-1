import random

file=open('randomintegers.txt','w')
for i in range(1,51):
    number=random.randrange(100,999)
    number=str(number)
    file.write(number)
    file.write('\n')
file.close()

file=open('randomintegers.txt','r')
print(file.read())