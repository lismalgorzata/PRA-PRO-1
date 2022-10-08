x=int(input("Liczba 1: "))
y=int(input("Liczba 2: "))

if x > 0 or y > 0: #3 operatory, które mają rożne priorytety operator porownania>operator logiczny
    print("Przyanjmniej jedna z liczb jest dodatnia")
else:
    print("Żadna z liczb nie jest dodatnia")
