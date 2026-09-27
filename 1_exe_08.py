'''
Write a program that ask the user to enter 3 numbers 
create variables called total and average that hold sum and average
'''

a = int(input("Enter first Number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

total = a+b+c
average = total/3

print(f"Total of three number is {total} and Average of three number is {average}")