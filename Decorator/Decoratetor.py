def decor(function):
    def inner(name):
        if name == "Somnath":
            print(name, "like pizza")
        else:
            return function(name)
    return inner

@decor
def process(name):
    print(name, "Like Burger")

process("abx")
process("cbv")
process("Somnath")
process("Akash")