queue = []

# add value at the end of the stack
def push(value):
    queue.append(value)
    
# remove the topmost element of the stack
# and return its value    
def get():
    if not empty():
        return queue.get()
    else:
        return None
    
# return true if the stack is empty
def empty():
    return len(queue) == 0

# display stack
def display():
    for i in queue:
        print(i, end=" ")
    print()