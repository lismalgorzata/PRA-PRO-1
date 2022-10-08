file=open('NumbersAndPowers.txt','w')
for i in range(1,11):
    secondpower=i**2
    thirdpower=i**3
    a=str(i)
    b=str(secondpower)
    c=str(thirdpower)
    file.write(a+',')
    file.write(b+',')
    file.write(c)
    file.write('\n')
file.close()

file=open('NumbersAndPowers.txt','r')
print(file.read())