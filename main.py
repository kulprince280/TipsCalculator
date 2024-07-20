print("welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
peoples = int(input("How many people to split the bill?"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
tip = bill * percentage / 100
total_bill = bill + tip
each_person = total_bill / peoples
print("Each person should pay: $" + str(each_person))




