cost = float(input("Enter the Price Of the Product: "))
sale = float(input("Enter The Sales Amount: "))

if (sale > cost):
    PAmount = sale - cost
    print("Profit = {0}".format(PAmount))
else:
    print("Loss!!")
    LAmount = sale - cost
    print("Loss = {0}".format(LAmount))