def bubblesort(array):
    n=len(array)
    while n > 1:
        for i in range(0, n-1):
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        n-=1
    return array

print(bubblesort([44,92,1,45,70]))
               
