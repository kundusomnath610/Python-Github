"""
    Reverse a String like hello... Using Iterative Method
"""

def rev_string(str):
    rev_string = 0
    for char in str:
        rev_string += char + rev_string
    return rev_string

print(rev_string(str))