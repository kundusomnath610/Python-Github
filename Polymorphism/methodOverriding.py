class Parent:
    def cook(self):
        print("Briyani")

    def learn(self):
        print("learn")

class Child(Parent):
    def play(self):
        print("child play")

    def learn(self):
        print("Learning Python")

c = Child()
c.play()

'''
    The Method which is derived from parent class and used as it is in child class, we call it as 
    Inherited Method.
    The Method which is only available for child class and not for parent class, such methods are
    called as Specialized Methods.
    The Methods which are derived from parent class and Modified into child class as per
    child class requriment , such methods are called as Overidden Methods.
'''