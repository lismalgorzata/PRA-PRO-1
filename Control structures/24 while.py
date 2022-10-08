x=int(input("x= "))
y=int(input("y= "))

i = 1
while i <= x :
    j = 1
    while j <= i:
        print("*", end = " ")
        j += 1
    print()
    i += 1
i = 1
while i <= y :
    j = y
    while j >= i:
        print("*", end = " ")
        j -= 1
    print()
    i += 1