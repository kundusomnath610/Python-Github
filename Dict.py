# d1 = {
#     'name': 'Priya',
#     'age': 20,
#     'Phone': 1234556,
#     'Math': 90,
#     'Science': 80,
#     'name': 'Anish'
# }
# print(d1, type(d1))
#
# ## Accessing value..
# print(d1['name'])
# print(d1['Math'])
#
#
# for i in d1.keys():
#     print(i) ## Print only keys.
#
# for i in d1.values():
#     print(i) ## print only values.
#
# for i in d1.items():
#     print(i) ## Item is whole dict print

contacts = {}

while True:
    entry = input("Enter the name and phone number: ")

    if entry.lower() == "done":
        break

    if "," in entry:
        name, phone = entry.split(",", 1)
        name = name.strip()
        phone = phone.strip()
        contacts[name] = phone
    else:
        print("Invalid number is 'name, phone'.")

print("\nContact List:")
for name, phone in contacts.items():
    print(f"{name}: {phone}")