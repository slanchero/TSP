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
    
    def reproduce(self,other:"Map"):
        son=Map()
        if self.score>other.score:
            son.add(other.cities[0])
            best =other
        else:
            son.add(self.cities[0])
            best = self
        #neighbors [3,2,3,4]
        #[0,1,2,4,3,5]74 , [0,1,4,2,3,5]82 = [0,1,2,4,3]
    
        
        for i in range(len(self.cities)-1):
            neighbors=[]
            neighbors.append(self.cities[i+1])
            neighbors.append(self.cities[i-1])
            neighbors.append(other.cities[i+1])
            neighbors.append(other.cities[i-1])
            
            min=float("inf")
            minCity=neighbors[0]
            
            for city in neighbors:
                if city not in son:
                    if self.distance(son.cities[-1],city)<min:
                        min = self.distance(son.cities[-1],city)
                        minCity = city
                    elif self.distance(son.cities[-1],city)==min:
                        if city.name.lower()==best.cities[i+1].name.lower():
                            min=self.distance(son.cities[-1],city)
                            minCity=city
            
            son.append(minCity)
        
        return son
            

    def mutate(self):
        check = True
        a = random.randint(0,len(self.cities)-1)
        while(check):
            b = random.randint(0,len(self.cities)-1)
            if(a!=b):
                check=False

        copy = self.cities[a]
        self.cities[a] = self.cities[b]
        self.cities[b] = copy
        self.evaluate()
    
    def _is_valid_operand(self, other):
        return (hasattr(other, "score"))

    def __eq__(self, map):
        if not self._is_valid_operand(map):
            return NotImplemented
        return (self.score==map.score)

    def __lt__(self, map):
        if not self._is_valid_operand(map):
            return NotImplemented
        return (self.score<map.score)

    def __le__(self, map):
        if not self._is_valid_operand(map):
            return NotImplemented
        return (self.score<=map.score)

    def __gt__(self, map):
        if not self._is_valid_operand(map):
            return NotImplemented
        return (self.score>map.score)
    
    def __ge__(self, map):
        if not self._is_valid_operand(map):
            return NotImplemented
        return (self.score>=map.score)

    def __contains__(self,city:City):
        for ciudad in self.cities:
            if ciudad.name.lower()==city.name.lower():
                return True
        
        return False