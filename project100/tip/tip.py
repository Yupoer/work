print("Welcome to the tip calculator.")
total = int(input("What wa the total bill?"))
people = int(input("How many people to split the bill?"))
percent_tip = float(input("What percentage tip would you like to give? 10, 12, or 15?"))/ 100
final = ((total * percent_tip)+ total) / people
print(f'Each person should pay: ${final:.2f}')
