input_string = input("Enter numbers separated by spaces: ")
numbers_list = list(map(int, input_string.split()))


numbers_tuple = tuple(numbers_list)


target = int(input("Enter a target number: "))


if target in numbers_tuple:
    index = numbers_tuple.index(target)
    print(f"The index of {target} in the tuple is: {index}")
else:
    print(f"{target} is not in the tuple.")
 