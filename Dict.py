d1 = {
    'name': 'Priya',
    'age': 20,
    'Phone': 1234556,
    'Math': 90,
    'Science': 80,
    'name': 'Anish'
}
print(d1, type(d1))

## Accesing value..
print(d1['name'])
print(d1['Math'])


for i in d1.keys():
    print(i) ## Print only keys..

for i in d1.values():
    print(i) ## print only values..

for i in d1.items():
    print(i) ## Item is whole dict print