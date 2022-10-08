import math
class surface_area():
    
    @staticmethod
    def triangle_area(side,height):
        area=0.5*side*height
        area=int(area)
        return area
    
    @staticmethod
    def circle_area(radius):
        area= math.pi * radius
        f_area="{:.2f}".format(area)
        return f_area
    
    @staticmethod
    def rectangle_area(a_side,b_side):
        area=a_side*b_side
        return area

print(surface_area.triangle_area(2,6))
print(surface_area.circle_area(3))
print(surface_area.rectangle_area(4,7))