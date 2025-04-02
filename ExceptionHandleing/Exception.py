def add(a, b):
    print("Start")
    print(a/b)
    print("End")

try:
    add(100, 10)
except:
    print("Exception Occured and handle.")
else:
    print("There is no exception")
finally:
    print("End")

print("Other Task")