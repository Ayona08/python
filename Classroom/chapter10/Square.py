import math

class Square:
    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side

    @property
    def perimeter(self):
        return 4 * self._side

    @property
    def area(self):
        return self._side ** 2

    @property
    def diagonal(self):
        return math.sqrt(2) * self._side

side_input = float(input("Enter the side length of the square: "))
square = Square(side_input)

print(f"Side: {square.side}")
print(f"Perimeter: {square.perimeter}")
print(f"Area: {square.area}")
print(f"Diagonal: {square.diagonal}")
