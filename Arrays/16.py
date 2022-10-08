#numbers=[12, 6, 4, 9, 3]
#for i in numbers:
 #   stars=i*"*"
  #  print(f"{i}:{stars}")

################################
numbers=[12, 6, 4, 9, 3]
for n in numbers:
    def stars(n):
        stars=n*"*"
        return stars
    print(f"{n}:{stars(n)}")
################################
def stars(n):
        stars=n*"*"
        print(n, end=': ')
        print(stars)
        return stars

numbers=[12, 6, 4, 9, 3]
for n in numbers:
    stars(n)
    
    
