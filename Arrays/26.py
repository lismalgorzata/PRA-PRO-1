array=[2,3,7,11,16,21,23,28,34,62,88,74,55]
n=len(array)
print("Array:",*array)

print("Even numbers:", end=" ")
for i in range(0,n):
    if (array[i])%2==0:
        print(array[i], end=" ")
print()
print("Odd numbers:", end=" ")
for i in range(0,n):
    if (array[i])%2 != 0:
        print(array[i], end=" ")
        
#####################################

array=[2,3,7,11,16,21,23,28,34,62,88,74,55]
n=len(array)
print("Array:",*array)
odd_numbers=[]
even_numbers=[]

for array_element in array:
    if array_element%2==0:
      even_numbers.append(array_element)
    else:
      odd_numbers.append(array_element)
print(even_numbers)
print(odd_numbers)