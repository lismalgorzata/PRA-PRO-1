import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
count=len(temperatures)
suma=0
for i in temperatures:
    i=int(i)
    suma=suma+i
average=suma/count

print('Average temperature is ',average,'C')
