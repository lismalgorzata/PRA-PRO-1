def number_count(number):
    suma=0
    for i in str(number):
        i=int(i)
        suma=suma+i
    return suma

x=number_count(5564)
print(x)