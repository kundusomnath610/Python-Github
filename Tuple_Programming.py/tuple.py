t1 = (10, 20, 20, True, 'Code')
print(t1, type(t1))

## Accesing element from tuple
print(t1[0])
print(t1[3])

#t1[0] = 300
#print(t1)

'''
    1. Tuple store homoginius and hetroginius data both.
    2. Tuple store duplicate value.
    3. Tuple is immutable..
'''

## Unpacking Tuple..
t2 = (100, 200, 300, 400)
e1, e2, e3, e4 = t2
print(f'e1: {e1}, e2: {e2}, e3: {e3}, e4: {e4}')

tup1 = (10, 20)
tup2 = (30, 40)
newtup = tup1 + tup2
print(newtup) ## (10, 20, 30, 40)
print(len(newtup))

