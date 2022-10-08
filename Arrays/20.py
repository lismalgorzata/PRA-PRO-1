import def20

number=23
print(f"Number: {number}")

array=[15, 38, 7, 23, 14]
print("Array:",*array)

result=def20.occurs(number, array)

if result==True:
    print(f"Result: number {number} appears in the array.")
else:
    print(f"Result: number {number} does not appear in the array.")