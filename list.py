number_list1 = input("Enter a number:").split() # 1, 2, 3
number_list2 = input("Enter a second number:").split() # 1, 2, 3, 4, 5

set1 = set(number_list1)
set2 = set(number_list2)

if set1.issubset(set2):
    print("Set 1 is subset of Set 2")
else:
    print("Set 1 is not Subset of Set 2")




