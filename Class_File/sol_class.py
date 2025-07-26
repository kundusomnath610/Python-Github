class Car:
    def __init__(self, brand, model): # Constructor and referring object
        self.brand = brand
        self.model = model

    def new_car(self): # This is a Method
        return f"Model: {self.model}, Brand: {self.brand}"

car1 = Car("Maruti", "Alto 800")
print(car1.model)
print(car1.brand)
print(car1.new_car())