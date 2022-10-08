def number_count(number):
    suma=0
    for i in str(number):
        i=int(i)
        suma=suma+i
    return suma

def number_count2(number):
    suma=0
    string_number=str(number)
    for cyfra in map(int,string_number):
        suma=suma+cyfra
    return suma

suma_cyfr=number_count(7182)
print(suma_cyfr)