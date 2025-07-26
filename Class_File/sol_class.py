class Car:
    def __init__(self, brand, model): # Constructor and referring object
        self.brand = brand
        self.model = model

    def new_car(self): # This is a Method
        return f"Model: {self.model}, Brand: {self.brand}"

    def fuel_type(self):
        return "Diesel and Petrol"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

new_car = ElectricCar("Tesla", "Model X", "5.0 Kv")
print(new_car.model)
print(new_car.brand)
print(new_car.battery_size)

car1 = Car("Maruti", "Alto 800")
print(car1.model)
print(car1.brand)
print(car1.new_car())