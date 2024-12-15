class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius**2
circle1 = circle(5)
print(circle1.area())
