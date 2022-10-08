array=[1,3,4,6,7,18]
parzyste=0
nparzyste=0
for i in array:
    if i%2==0:
        parzyste+=1
    else:
        nparzyste+=1

print(f"Parzystych: {parzyste}, nieparzystych: {nparzyste}")