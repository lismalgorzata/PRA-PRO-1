number=16
array=[1,3,7,14,32,63,12,88,54,31,19,5,2]
n=len(array)
print(f"Numbers grater than {number} are:", end=" ")
for i in range(0,n):
    if number<array[i]:
        print(array[i], end=" ")