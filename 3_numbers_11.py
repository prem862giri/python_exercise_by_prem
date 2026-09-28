#Write a program that asks the user to enter a weight in kilograms.
#The program should convert it to pounds
#printing the answer rounded to the nearest tenth of a pound.

weight_kg = float(input("Enter your weight in kg: "))

weight_pound = 2.2 * weight_kg

final_weight = round(weight_pound,1)
print(f"Weight in pounds: {final_weight}")