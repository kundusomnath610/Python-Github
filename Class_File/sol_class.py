class Car:
    total_car = 0
    def __init__(self, brand, model): # Constructor and referring object
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def new_car(self): # This is a Method
        return f"Model: {self.model}, Brand: {self.brand}"

    """
        Polymorphism for fuel_type method function in Car Class
    """
    def fuel_type(self): # Polymorphism for Car Class
        return "Diesel and Petrol"

    @staticmethod
    def general_description(): # Static Method function cause it i in Class
        return "Car Mode of transport"

    # @property
    # def model(self):
    #     return self.__model

class ElectricCar(Car): # Inheriting the Car class Property
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    """
        Polymorphism for fuel_type method function in ElectricCar Class
    """
    def fuel_type(self): # Polymorphism
        return "Electric Charge"

new_car = ElectricCar("Tesla", "Model X", "5.0 Kv")
print(new_car.model)
print(new_car.brand)
print(new_car.battery_size)
print()

car1 = Car("Maruti", "Alto 800")
car2 = Car("Nissan", "Mustang")
print(car1.model)
print(car1.brand)
print(car1.new_car())
print(car2.brand)
print(car2.model)
print()

print(Car.total_car)

class Battery:
    def battery_info(self):
        return "This is best Battery"

class Engine:
    def engine_info(self):
        return "This is engine info"

class Ninja(Battery, Engine, Car):
    pass

ninja_bike = Ninja("Kawasaki", "Ninja 650 RR")
print(ninja_bike.battery_info())
print(ninja_bike.engine_info())