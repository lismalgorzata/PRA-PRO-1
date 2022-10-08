colors=["orange","pink","blue",'yellow','violet']

file=open("colors.txt", 'w')

for color in range(0, len(colors)):
# for film in film_titles:
    file.write(colors[color])
    #file.write(film)
    file.write("\n")
file.close()

file=open('colors.txt', 'r')
print(file.read())