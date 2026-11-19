print()
height = float(input("Enter your Height in Centimeters: "))
weight = float(input("Enter your Weight in Kilograms: "))

BMI = weight / (height / 100)**2

print("BMI is", BMI)

if BMI <= 18.4:
    print("Your Under weight...")
elif BMI <= 24.9:
    print("You are Healthy...")
elif BMI <= 29.9:
    print("Your Over Weight...")
elif BMI <= 34.9:
    print("You are Severly Over Weight...")
elif BMI <= 39.9:
    print("You are Obese...")
else:
    print("You are Severly Obese")