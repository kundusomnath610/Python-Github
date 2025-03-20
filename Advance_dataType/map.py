li = [1, 2, 3, 4, 5]

def square(ele):
    return ele * ele

result = map(square, li)
print(result)

print(list(result))

li2 = ['10', '20', '30', '40']
print(li2) ## ['10', '20', '30', '40'] form of string
new_li = list(map(int, li2))
print(new_li) ## [10, 20, 30, 40] from of integer


li3 = [30, 40, 50, 60]
print(list(map(float, li3))) ## [30.0, 40.0, 50.0, 60.0]

print(list(map(bool, li3)))  ## [True, True, True, True]