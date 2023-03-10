import math
import random
class City:
    def __init__(self,name):
        self.name=name
        self.x = 0
        self.y = 0
        
    
    def addX(self,x):
        self.x=x
    
    def addY(self,y):
        self.y=y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
class Map:
    def __init__(self):
        self.cities=[]
        self.score=0
    
    def add(self, city):
        self.cities.append(city)

    def evaluate(self):
        total=0
        i=0
        while(i<self.cities.__len__()-1):
            total = total + self.distance(self.cities[i],self.cities[i+1])
            i = i+1
        total = total + self.distance(self.cities[i],self.cities[0])
        self.score=total
    
    def distance(self,cityA:City, cityB:City):
        return math.sqrt((cityA.x-cityB.x)**2+(cityA.y-cityB.y)**2)

    def mutate(self):
        check = True
        while(check):
            a = random.randint(0,self.cities.__len__()-1)
            b = random.randint(0,self.cities.__len__()-1)
            if(a!=b):
                check=False

        copy = self.cities[a]
        self.cities[a] = self.cities[b]
        self.cities[b] = copy