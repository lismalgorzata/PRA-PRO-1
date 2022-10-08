array=[8, 2, 5, 1, 9]
print("array:", *array)

print("2nd power:", end=" ")
for i in array:
    pow=i**2
    print(pow, end=" ")