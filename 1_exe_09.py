'''
Ask the user for the price of the meal and the percent tip they want to leave.
print both the tip amount and the total bill with tip included'''

price = int(input("Enter meal actual price: "))
tip_percent = float(input("Tip percent customer wants to pay: "))

tip_amount = price * tip_percent /100
total = price+tip_amount

print(f"The tip amount is {tip_amount} and the total bill with tip amount is {total}.")