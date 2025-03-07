from dataclasses import dataclass, field

@dataclass
class Employee:
    salary : float = field(default=5000)
    names: list = field(default_factory=list)
    department : str = field(default='IT', repr = True)

e1 = Employee()
print(e1.salary)

e1.names.append("Animesh")
print(e1)