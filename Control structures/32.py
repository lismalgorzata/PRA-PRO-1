for i in range(1,8):
    last=0
    for j in range(1,50,7):
        if j==1:
            last=i
            print(i, end=" ")
        else:
            last+=7
            print(last, end=" ")
    print()
       