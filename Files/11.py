film_titles=["John Wick", "John Wick 2", "John Wick 3", "Spiderman: Homecoming", "Spiderman: No way home"]

file=open("Films.txt", 'w')

for film in range(0, len(film_titles)):
# for film in film_titles:
    file.write(film_titles[film])
    #file.write(film)
    file.write("\n")
file.close()

file=open('Films.txt', 'r')
print(file.read())