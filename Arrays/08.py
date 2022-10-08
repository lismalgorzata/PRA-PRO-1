array=[-15,8,-31,47,-2,19]
maks=max(array)
mini=min(array)

print(f"Maksymalna : {maks}, minimialna: {mini}")
------------------------------------------
max=array[0]
min=array[0]

for i in array:
    if i<min:
        min=i
    if i>max:
        max=x

print(max)
print(min)