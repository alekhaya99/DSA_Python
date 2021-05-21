import math
'''
Question 2
 Create a circle class that will take the value of a radius and 
 return the area of the circle
'''

class Area(object):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        a=2*math.pi*self.radius**2
        return a

b=Area(5)
print(b.area())