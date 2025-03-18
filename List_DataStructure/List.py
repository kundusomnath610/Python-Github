li1 = [10, 20, 30, 'code', True, 66.7] ## List is mutable
print(li1, type(li1))

print(li1[0], end=" ")
print(li1[1], end=" ")
print(li1[2], end=" ")
print(li1[3], end=" ")
print(li1[4], end=" ")

li1[3] = "MyCode"
print("After update:-", li1)

'''
1.In List we can store Homogeneous(Data with similar Data Type) as well as 
Heterogeneous (Data with different Data Type) Type of Data.

2.List is an Ordered Collection of Data. List Maintains order of insertion in the output
as it is thats why we call it as ordered collection of Data.

3.In List we can Store duplicate values.

4. Lists are Mutable means once we declare the list we can modify it.
'''