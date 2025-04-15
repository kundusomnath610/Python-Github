rows = int(input())

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")

    ch = ord('A')
    for j in range(i + 1):
        print(chr(ch + j), end="")

    for j in range(i - 1, -1, -1):
        print(chr(ch + j), end="")

    print()