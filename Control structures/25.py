a=int(input("wprowadz a: "))
b=int(input("wprowadz b: "))

for i in range (1,(a+1)):
    for j in range (1,(b+1)):
        if i==1 or i==a or j==1 or j==b :
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
      