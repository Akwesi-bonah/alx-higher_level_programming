from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: str


john = Employee('john', 'ICT', 100)

print(john.dept)