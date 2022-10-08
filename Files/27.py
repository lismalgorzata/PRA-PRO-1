import re
with open('sample1.txt') as file:
    for line in file:
        result=re.findall('\w{6,}',line)
        #print(*result)
        for i in result:
            print(i+'\n', end="")
        