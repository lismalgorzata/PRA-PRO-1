amount=int(input("Enter the amount in PLN: "))
print(f"The amount of PLN {amount} in coins:")
#ile 5zl
a=amount//5
print(f"5zł: {a}")
#ile reszty
if a%5 == 0:
    print("2zł: 0")
    print("1zł: 0")
else:
    b=amount%5
    #ile 2zl
    c=b//2
    print(f"2zł: {c}")
    #ile 1zl
    if b%2 == 0 :
        print("1zł: 0")
    else:
        d=b%2
        print(f"1zł: {d}")

    



   