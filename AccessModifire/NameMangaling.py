class Demo:
    def __init__(self):
        self.__x = 100 ## it act look like private variable..
    def disp(self):
        print(self.__x) # 100

d = Demo()
d.disp()
print("Accessing the private variable outside the class: ", d._Demo__x)

'''
    Is the process of giving new name to the private variable in format of: __classname__variablename..

    If we want to access private vari out side the class than use: _classname__variablename..
'''