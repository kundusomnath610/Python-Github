class GrandParent:
    def cook(self):
        print("Briyani")

class parent(GrandParent):
    def cook(self):
        print("paulo")

class Child(parent):
    def cook(self):
        print("Maggie")
        super().cook()
        super(parent, self).cook()

c = Child()
c.cook()