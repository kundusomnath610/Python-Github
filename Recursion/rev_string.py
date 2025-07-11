"""
    Reverse a String like hello... Using Iterative Method
"""
str = "somnath"

def reverse_string(str):
    rev_string = ""
    for char in str:
        rev_string = char + rev_string
    return rev_string

print(reverse_string(str))
