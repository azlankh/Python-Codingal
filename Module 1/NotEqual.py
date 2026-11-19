a = 10
b = 12
c = 14

print(not a == b)

print(not b == c)

a = "Azlan"
b = "Python"

if (not a == b):
    print("A and B are not Equal....")
else:
    print("They are Equal....")

a = 12.21
b = 67

if (a == 1) == (b == 5):
    print("Hello!!")

a = int(input("Enter a Number: "))

if not (a % 2 == 0):
    print(a, "is a Odd Number")
else:
    print(a, "is a Even Number")