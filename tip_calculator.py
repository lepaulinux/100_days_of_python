print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# solution 1
# Convert the tip percentage to decimal
tip_decimal = tip / 100
# Calculate the tip amount
tip_amount = bill * tip_decimal
# Calculate the total bill including the tip
total_bill = bill + tip_amount
# Calculate how much each person should pay
total_per_person = total_bill / people
# Print the result rounded to 2 decimal places
print(f"Each person should pay: {round(total_per_person, 2)}")

'''
# solution 2
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay {final_amount}")
'''
