rows = int(input("Enter a number:- "))

for i in range(1, rows + 1):
    for j in range(i):
        print(chr(ord('1') + j), end=" ")
    print()