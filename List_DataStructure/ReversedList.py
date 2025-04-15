# TODO: Allow the user to enter a list of numbers and store it in numbers_list
numbers_list = input("Enter numbers without spaces (e.g., 12345): ")

# TODO: Convert the input string into a list of integers
numbers = [int(ch) for ch in numbers_list]

# TODO: Use list slicing to reverse the list and print it
reversed_numbers = numbers[::-1]

print("Reversed list:", reversed_numbers)
