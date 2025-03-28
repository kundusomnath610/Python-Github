class Calsi:
    def calculate(self, a,b):
        print('calculating a and b')

class Add(Calsi):
    def calculate(self, a, b):
        print(a+b)

class Mul(Calsi):
    def calculate(self, a, b):
        print(a * b)

class div(Calsi):
    pass

def permit(ref):
    ref.calculate(10, 20)