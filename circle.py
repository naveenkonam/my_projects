class Circle():

    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi
    
    def setradius(self,radius):
        self.radius = radius
    
    def getradius(self):
        return self.radius

x= Circle()

print(x.getradius())
print(x.area())
