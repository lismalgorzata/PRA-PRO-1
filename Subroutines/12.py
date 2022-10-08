def funkcja(N):
    for i in range(1, N+1):
        a1=1
        an=N
        suma=((a1+an)/2)*N
        return suma
N=10
suma_wszystkich=funkcja(N)
print(suma_wszystkich)