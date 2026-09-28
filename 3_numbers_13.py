# asks the user for a number 
#prints out the sine, cosine, tangetof that number

from math import *

n = int(input("Enter a number: "))

sine_number = sin(n)
print(f"The sine number of {n} is {sine_number}")

cosine_number = cos(n)
print(f"The cosine number of {n} is {cosine_number}")

tanget_number = tan(n)
print(f"The tanget number of {n} is {tanget_number}")