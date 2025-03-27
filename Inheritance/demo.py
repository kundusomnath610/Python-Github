class Demo1:
    def Disk1(self):
        print("Somnath1")

class Demo2:
    def Disk2(self):
        print("Somnath2")

class Demo3(Demo1, Demo2):
    def Disk3(self):
        print("Somnath Kundu3")

   
d3 = Demo3()
d3.Disk1()
d3.Disk2()
d3.Disk3()

## MRO(Method Resolution Order) the order in which method searched in multiple inheritance Scenario...