userData = input("Enter List Element:- ")
li = userData.split()
print(li)

newli = []

for i in li:
    newli.append(int(i))

print(sum(newli)/len(newli))