array=[2, 3, 2, 5, 8, 1, 9, 8,2]

print("Array:", end=" ")
unique_numb=[]
not_unique_numb=[]
for i in array:
    print(i, end=" ")
print()
#print("Array:",*array)
for i in array:
    if i in unique_numb:
        unique_numb.remove(i)
        not_unique_numb.append(i)
    else:
        if i not in not_unique_numb:
            unique_numb.append(i)
print("Unique numbers: ",*unique_numb)