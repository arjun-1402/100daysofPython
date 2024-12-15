print("Welcome to the tip calculator!")

# Get inputs from the user
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate the total tip and bill per person
tip_amount = bill * (tip_percentage / 100)
total_bill = bill + tip_amount
bill_per_person = total_bill / people

# Format the result to 2 decimal places
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")
