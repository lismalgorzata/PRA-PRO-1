import re

with open('grades.txt') as file:
    for line in file:
        result=re.findall('\d.\d',line)
        suma=0
        count=len(result)
        for i in result:
            i=float(i)
            suma=suma+i
            arithmetic_mean=(suma/count)
            f_art_mean="{:.2f}".format(arithmetic_mean)

print("Arithmetic mean of student's grade is: ", f_art_mean)
        
    