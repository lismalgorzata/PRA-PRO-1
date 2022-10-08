text="You never get a second chance to make a first impression"

def letter_count(text, e):
    count=0
    for litera in text :
        if litera == e:
            count +=1
    return count

print(letter_count(text, 'e'))
    
