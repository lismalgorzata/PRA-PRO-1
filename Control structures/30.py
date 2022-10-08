N=int(input("Wprowadź ilość liczb: "))

n=2
licznik=0
while licznik<N :
    is_prime= True
    for dzielnik in range (2,n):
        if (n%dzielnik) == 0 :
            is_prime= False   
            break
    if is_prime is True:
        print(n, end=" ")
        licznik+=1
    n+=1
         
