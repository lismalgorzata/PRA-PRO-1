class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y

    @staticmethod
    def calculate_distance(point1,point2):
        if point1==point2:
            return 'Distance equals 0'
        else:
            distance=((point2.x-point1.x)**2+(point2.y-point1.y)**2)**0.5
            return f'Distance: {distance}'

point1=Point(2,3)
point2=Point(2,8)

print(Point.calculate_distance(point1,point2))