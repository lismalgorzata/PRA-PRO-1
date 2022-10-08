array=[15, 8, 31, 47, 2, 19]
print("existing array:",*array)

print("reversed array:", end=" ")
for i in range(len(array)-1, -1, -1):
    print(array[i], end=" ")
    