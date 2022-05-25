# Write a Python calculator that can perform:
# addition, subtraction, division, multiplication and modulus operations.
#  It should accept user input

print("My simple Calculator: ensure to input a number")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

choice = int(input("Enter what you want to perform:(1)addition (2)subtraction (3)division (4)multiplication (5)modulus: "))
if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1/num2)
elif choice == 4:
    print(num1 * num2)
elif choice == 5:
    print(num1 % num2)