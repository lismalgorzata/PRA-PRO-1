x=int(input("x= "))
y=int(input("y= "))

if x>0 and y>0:
    print(f"Point {x},{y} is in the first quadrant of the coordinate system.")
elif x<0 and y<0:
    print(f"Point {x},{y} is in the third quadrant of the coordinate system.")
elif x>0 and y<0:
    print(f"Point {x},{y} is in the fourth quadrant of the coordinate system.")
elif x<0 and y>0:
    print(f"Point {x},{y} is in the second quadrant of the coordinate system.")
elif x==0 and y!=0:
    print(f"Point {x},{y} is in the x axis.")
elif x!=0 and y==0:
    print(f"Point {x},{y} is in the y axis.")
else:
    print(f"Point {x},{y} is in the (0,0) point.")