import stack
expression= 2+3
stack=[]
while True:
    x=input("znak: ")
    if x == "+":
        y=stack.pop()
        w=stack.pop()
        z=w+y
        stack.append(z)
    elif x == "-":
        y=stack.pop()
        w=stack.pop()
        z=w-y
        stack.append(z)
    elif x == "*":
        y=stack.pop()
        w=stack.pop()
        z=w*y
        stack.append(z)
    elif x == "/":
        y=stack.pop()
        w=stack.pop()
        z=w/y
        stack.append(z)
    elif x == "=":
        y=stack.pop()
        print(y)
    else:
        stack.append(int(x))