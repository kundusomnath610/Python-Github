# Take input from the user and convert to list of integers
num_list1 = list(map(int, input("Enter numbers for List 1 (space-separated): ").replace(","," ").split()))
num_list2 = list(map(int, input("Enter numbers for List 2 (space-separated): ").replace(","," ").split()))

# Convert lists to sets
set1 = set(num_list1)
set2 = set(num_list2)

# Find common elements using intersection
common_element_set = set1.intersection(set2)

# Sort the result
sorted_common_elements = sorted(common_element_set)

# Print the result
print("Common elements:", sorted_common_elements)
