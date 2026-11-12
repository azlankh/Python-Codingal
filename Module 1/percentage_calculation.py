hindi = int(input("Enter Marks of Hindi: "))
eng = int(input("Enter Marks of English: "))
maths = int(input("Enter the Marks of Maths: "))
sci = int(input("Enter the Marks of Science: "))
print()
total_marks = hindi+sci+maths+eng
print("Your Total Marks is ", total_marks,"/ 400")
percentage = (total_marks / 400) * 100

print("Overall Percentage is ", percentage)