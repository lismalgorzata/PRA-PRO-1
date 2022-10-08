array=[5,4,3,2,6,5]
print(f"Array: {array} ")

string_array= [str(element) for element in array]
array_commas=",".join(string_array)

print(f"String: {array_commas}")
####################

print("String:", end=" ")
print(*array, sep=",")
