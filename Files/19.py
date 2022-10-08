maf=open('MeatAndFish.txt','r')
gab=open('GrainsAndBread.txt','r')

file=open('shoppinglist.txt','w')
for line in maf:
    file.write(line)
for line in gab:
    file.write(line)
maf.close()
gab.close()
file.close()

file=open('shoppinglist.txt','r')
print(file.read())
