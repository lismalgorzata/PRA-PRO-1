def mediana(array):
    n=len(array)
    while n > 1:
        for i in range(0, n-1):
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        n-=1
    n=len(array)
    if (n%2)!=0 :
        index=int(n/2)
        return array[index]
    else:
        index1=int((n/2)-1)
        index2=int((n/2))
        median=(array[index1]+array[index2])/2
        return median
            
print(mediana([6,8,3,1,0,5,7]))