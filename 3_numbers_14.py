#asks the user to enter an angle in degrees 
# print out the sine of that angle

from math import *

n = float(input("Enter an angle in degrees: "))

radians_number = radians(n)
sine_value = sin(radians_number)
print(f"The sine of {n} degrees is {sine_value}.")

