from dataclasses import dataclass
@dataclass
class Point:
    x: float
    y: float
p1 = Point(x=1,y=2)
p2 = Point(x=3,y=4)
p1==p2
print(p1)
print(p2)


