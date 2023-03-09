class City:
    def __init__(self,name):
        self.name=name
    
    def addX(self,x):
        self.x=x
    
    def addY(self,y):
        self.y=y
    
class Map:
    def __init__(self):
        self.cities=[]
    
    def add(self, city):
        self.cities.append(city)