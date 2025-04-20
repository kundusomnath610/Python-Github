li = [10, 20, 30, 40]
sq = []

## for loop
for i in li:
    sq.append(i ** 2)
print("The square is: ", sq)
print([i ** 2 for i in li])

## WAP to +5 in the list
print([i + 5 for i in li])

li1 = [1, 2, 3, 4, 5]
print([i for i in li1 if i%2 == 0])
print()

'''
    This is the bad idea to create nested list..
    cause when i access the list id it print same..
'''

list = [[]] * 5
for list1 in list:
    print(id(list1))
