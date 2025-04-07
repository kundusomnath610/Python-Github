def smart(function):
    def inner(a, b):
        if b == 0:
            print("Not Possible")
        else:
            return function(a, b)
    return inner

@smart
def div(a, b):
    print(a/b)

div(10, 2)
div(20, 5)
div(100, 5)