balance = 5000.25
cust = input("What is your name? ")
print("Welcome " + cust + ", your balance is $" + str(balance))
pay = input("How much would you like to deposit?")
balance += float(pay)
print("Your balance is now $" + str(balance))