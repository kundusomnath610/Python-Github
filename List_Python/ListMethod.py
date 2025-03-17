li = [50]
# Adding element into the list
li.append(100)
print(li)


'''
    1. pop() method return element with help of index value.
    2. remove() method remove the element without index value.
    3. del() method remove the element with help of index, 
        But it is a keyword, and it dosen't return anything
'''

li.insert(0, 500)
print(li)

## POP () 
ele = li.pop()
print(ele)
print(li)

print(li.pop(0))
print(li)

li.append(700)

li.remove(700)
print(li)

li.append(900)
print(li)

# Del Keyword
del li[1]
print("After del:", li)

# del li ## Delete whole object from the memory
# print(li) ## print the list

