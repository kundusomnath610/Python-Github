def dis():
    print("start")
    yield 10
    print("task 1")
    yield 20
    print('Task 2')
    yield 30
d = dis()
print(d)

print("final")