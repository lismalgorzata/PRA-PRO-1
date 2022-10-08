imiona=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

print("Imiona:",*imiona)

imie=len(imiona[0])
for i in range(1, (len(imiona)-1)):
    kolejne_imie=len(imiona[i])
    if kolejne_imie>imie:
        najdluzsze_imie=imiona[i]
print("Najdłuższe imię:" + najdluzsze_imie)
    
    