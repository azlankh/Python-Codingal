print("What is the Total Amount of Money do you want to Withdraw?")
amount = int(input("Input Above 100: "))
actual_amount = amount
note_1 = amount // 100
amount = amount % 100
note_2 = amount // 50
amount = amount % 50
note_3 = amount // 10

print("No of 100 Notes in ", actual_amount, "are ", note_1)
print("No of 50 Notes in ", actual_amount, "are ", note_2)
print("No of 10 Notes in ", actual_amount, "are ", note_3)