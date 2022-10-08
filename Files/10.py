file=open('mojedane.txt', 'w')
file.write("""Małgorzata
Lis
UEK
Informatyka
""")
file.close()
file=open('mojedane.txt', 'r')
print(file.read())

# \n znak nowej linii