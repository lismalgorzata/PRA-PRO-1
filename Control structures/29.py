liczba= int(input("Enter number: "))
licznik=1
suma=0
while liczba>0 :
    kolejnaliczba=int(input("Enter number: "))
    suma=suma+kolejnaliczba
    licznik += 1
    if kolejnaliczba==0 :
        break
    
ilosc=licznik-1
print(f"Quantity: {ilosc}", end=" ")
sum=liczba+suma
print(f"Sum: {sum}", end=" ")
srednia=sum/ilosc
print(f"Mean: {srednia}", end=" ")

        