i = 1
while(i <= 11):
    print(i, end = " ")
    i = i+1
print()
## for Loop
for i in range(1, 6):
    if(i == 3):
        continue
    else:
        print(i, end = " ")
print()
## print 1 to 10 if number is 5 then break the loop
for i in range(1, 10):
    if(i == 5):
        break
    else:
        print(i, end = " ")

print()
## WAC to print a user input number and print this number table..
num = int(input("Enter the table number: "))
for i in range(1 , 11):
    print(i * num, end = " ")