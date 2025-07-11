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


"""
    Recursive Approch to reverse string...
"""

str = "Hello"

def rev_string(str):
    if len(str) <= 1:
        return str
    
    return rev_string(str[1:]) + str[0]
print(rev_string(str))
