def dis():
    yield 10
    yield 20
    yield 30

res = dis()
print(res)
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())