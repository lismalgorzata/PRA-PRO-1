def przedostatnia(array):
    n=len(array)
    while n > 1:
        for i in range(0, n-1):
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        n-=1
    przedostatnia=array[len(array)-2]
    return przedostatnia

array= [5,1,9,6,1]
print("Array:",*array)
print(f"Result: {przedostatnia(array)}")