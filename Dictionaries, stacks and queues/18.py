def push(value):
    stack.append(value)
      
def pop():
    if not empty():
        return stack.pop()
    else:
        return None
    
def empty():
    return len(stack) == 0

def display():
    return ' '.join(str(e) for e in stack)

def read():
    return stack[len(stack)-1]

def convert(number):
    remainder=number%2
    if remainder == 0:
        number /=2
        push(0)
    else:
        number=(number-1)/2
        push(1)
    
    if number==0:
        return
    
    convert(number)
    return 
    
stack = []
number=18
convert(18)

print(f"Natural number: {number}")
print(f"Binary number: ",end="")

for i in range(len(stack)):
    print(read(),end="")
    pop()
 