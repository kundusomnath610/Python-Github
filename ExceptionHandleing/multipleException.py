def process(a, b):
    print(a / b)
try:
    process(10, "code")
except ZeroDivisionError:
    print("Zero Division error occured and handle")
except KeyError:
    print("Name error handle")
except TypeError:
    print("fjkn")
except:
    print("Last eception")
print("Task Over")