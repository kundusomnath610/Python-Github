"""
    Recursive approch without loop...
"""

arr = [4, 5, 2, 9, 10]

def sum_of_array(arr):
    if arr == 0:
        return 0
    
    return arr[0] + sum_of_array(arr[1:])

