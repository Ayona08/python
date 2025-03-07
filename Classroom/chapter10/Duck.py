from CommissionEmployee import CommissionEmployee
from SalariedCommissionedEmployee import SalariedCommissionedEmployee
class Duck:
    def __init__(self):
        self.quack = "Quack!"
    def earning(self):
        return "Duck is earning money"
    def __str__(self):
        return "I am a well paid Duck."
    
d = Duck()
cel = CommissionEmployee("Animesh", "Patra", 2241016255, 90000, 0.5 )
scel = c2 = SalariedCommissionedEmployee("Animesh", "Patra", 2241016255, 90000, 0.5, 100000 )

L = [d, cel, scel]
for i in L:
    print(i.earning())
    print(i.__str__())
    