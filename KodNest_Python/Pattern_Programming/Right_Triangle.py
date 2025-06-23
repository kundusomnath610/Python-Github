row = int(input("Enter a row:- "))
for i in range(1 ,row + 1):
    for j in range(i):
        print("*", end=" ")
    print()