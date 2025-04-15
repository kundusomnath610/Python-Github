def print_hollow_diamond():
    rows = int(input("Enter the number of rows (half of the diamond height): "))

    # Upper half of the diamond (including the middle line)
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Lower half of the diamond (same number of lines as upper)
    for i in range(rows, 0, -1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Run the function
print_hollow_diamond()
