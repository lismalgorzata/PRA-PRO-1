file=open('shopping.txt','a')
a=input('Podaj produkt: ')
file.write(a+'\n')
file.close()

file=open('shopping.txt', 'r')
print(file.read())

#append dodaje na koncu
#jak na początku: otwieramy plik, całość do odczytu, odczyt, duży string,
#ten sam plik do oczytu i mleko na początku
#jakas tam sic? sik? nie wiem google go
