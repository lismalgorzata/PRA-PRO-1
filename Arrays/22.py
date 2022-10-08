def roznica(array):
    n=len(array)
    while n > 1:
        for i in range(0, n-1):
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        n-=1
        roznica= array[-1] - array[0]
    return roznica
    
array= [5,1,9,6,1]
print("Array:",*array)
############
maks=max(array)
mini=min(array)
roznica=maks-mini
print(f"Result: {roznica}")
######################

print(f"Result: {roznica(array)}")