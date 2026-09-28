#one way to find out the last digit of a number is to mod the number by 10
# Write  a program that asks the user to enter a power.
# Then find the last digit of 2 raised to that power

from math import *

n = int(input("Enter a exponent: "))

power = 2**n
print(f"Power of 2 with exponent{n} is {power}")

last_digit = power%10
print(f"The last digit is {last_digit}")



#last two digit
last_two_digit = power%100
print(f"Last Two digit of result is {last_two_digit}")



#How many last digit wants by user
digit_want = int(input("How many last digit wants? "))
n_digit = power%(10**digit_want)
print(f"User wants last {digit_want} digits, which is {n_digit}")