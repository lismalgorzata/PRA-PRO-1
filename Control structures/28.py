##Fibonacci sequence:

n1=0
n2=1
licznik=2
suma=0
print(n1, n2, end=" ")
while licznik <=50 :
    suma=n1+n2
    n1=n2
    n2=suma
    licznik += 1
    print(suma, end=" ")
    
