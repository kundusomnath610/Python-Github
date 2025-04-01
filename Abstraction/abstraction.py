from abc import ABC, abstractmethod

class Animal(ABC):
    pass

# This is allowed because Animal has no abstract methods
a1 = Animal()

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass


'''
    Rule 3:- If an abstract class contains only concrete methods, 
    then an object can be created, and concrete methods can be invoked.
'''
class Animal2(ABC):
    def eat(self):
        print("Inside eat")

# This is allowed because Animal2 has only concrete methods
a3 = Animal2()
a3.eat()

'''
    Rule 4:- If a class is derived from an abstract class and does not implement 
    all abstract methods, then an object of the derived class cannot be created.
'''

class Animal4(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

# This class is incomplete because it does not implement `sleep()`
class Child(Animal4):
    def eat(self):
        print("Inside eat")

# c = Child()  # Not allowed: Child must implement `sleep()`

# Properly implementing `sleep()`
class FullyImplementedChild(Animal4):
    def eat(self):
        print("Inside eat")

    def sleep(self):
        print("Inside sleep")

# Now, this works:
c2 = FullyImplementedChild()
c2.eat()
c2.sleep()
