weight = int(input("Enter weight: "))
height = float(input())

result = weight / (height ** 2)

if result >= 30:
    print("You are in Obese category.")
elif result >= 25 and result <= 29.9:
    print("You are in the Overweight category.")
elif result >= 18.5 and result <= 24.9:
    print("You are the normal weight category.")
elif result <= 18.5:
    print("You are in the underWeight Category.")