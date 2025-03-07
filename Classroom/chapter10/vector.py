class Vector:
    def __init__(self, *components):
        self.components = components

    def leng(self):
        return len (self.components)
    
    def dist(self):
        return sum(x**2 for x in self.components)**0.5
    
    def __add__(self, other):
        return Vector(*[x+y for x, y in zip(self.components, other.components)])
    
    def __sub__(self, other):
        return Vector(*[x-y for x, y in zip(self.components, other.components)])

    def __mul__(self, scalar):
        return Vector(*[x*scalar for x in self.components])
    
    def __truediv__(self, scalar):
        return Vector(*[x/scalar for x in self.components])
    
    def __lt__(self, other):
        return self.dist() < other.dist()
    
    def __eq__(self, other):
        e = [x < y for x,y in zip(self.components, other.components)]
        for tv in e:
            if tv == False :
                return False
        return True   
    
    def __repr__(self):
        return f'Vector{self.components}'
    # Define the Vector class
class Vector:
    def __init__(self, *components):
        self.components = components

    def leng(self):
        return len(self.components)
    
    def dist(self):
        return sum(x**2 for x in self.components)**0.5
    
    def __add__(self, other):
        return Vector(*[x+y for x, y in zip(self.components, other.components)])
    
    def __sub__(self, other):
        return Vector(*[x-y for x, y in zip(self.components, other.components)])

    def __mul__(self, scalar):
        return Vector(*[x*scalar for x in self.components])
    
    def __truediv__(self, scalar):
        return Vector(*[x/scalar for x in self.components])
    
    def __lt__(self, other):
        return self.dist() < other.dist()
    
    def __eq__(self, other):
        e = [x == y for x, y in zip(self.components, other.components)]
        for tv in e:
            if tv == False:
                return False
        return True   
    
    def __repr__(self):
        return f'Vector{self.components}'

v1 = Vector(1, 2, 3, 4, 5)
v2 = Vector(0, 9, 8, 7)

print(f'v1: {v1}')
print(f'v2: {v2}')

print(f'Length of v1: {v1.leng()}') 

print(f'Distance (magnitude) of v1: {v1.dist()}')  

print(f'v1 + v2: {v1 + v2}')  

print(f'v1 - v2: {v1 - v2}') 

print(f'v1 * 5: {v1 * 5}')  

print(f'v1 / 2: {v1 / 2}') 

print(f'v1 < v2: {v1 < v2}')

print(f'v1 == v2: {v1 == v2}')  




