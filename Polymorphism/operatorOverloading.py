class Student:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def __add__(self, other):
        return self.name + other.name
    def __truediv__(self, other):
        return self.name + other.name
    
s1  = Student("Hello")
print(s1)

s2  = Student(" Somnath")
print(s2)

print(s1 / s2)