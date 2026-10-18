# Day 2: Tip Calculator Project

print("Welcome to the Tip Calculator!")

# 1. Get user inputs
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# 2. Perform the calculations
tip_amount = bill * (tip_percentage / 100)
total_bill = bill + tip_amount
bill_per_person = total_bill / people

# 3. Format the result to 2 decimal places
final_amount = "{:.2f}".format(bill_per_person)

# 4. Print the final split amount
print(f"Each person should pay: ${final_amount}")