class Vehicle:
    def __init__(self, make, model, is_available):
        self.make = make
        self.model = model
        self.is_available = is_available

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Status: {self.is_available}")

    def mark_rented(self):
        print()