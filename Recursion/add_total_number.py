"""
    Itrrative approch with Loop.. Recursion problem
"""

arr = [5, 6, 7, 2, 10]

def number_iterative(arr):
    total = 0
    for num in arr:
        total += num
    return total

print(number_iterative(arr))