from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    salary : float = field(default=5000)
    department : str = field(default='IT', repr = False)

p1 = Person("Animesh", 300000)
print(p1.name)
