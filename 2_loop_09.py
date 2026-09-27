#ask how many Fibonacci numbers to print, where first 2 number are 1,1.

a = 1
b = 1
fib = 0

print_time = int(input("Enter How Much Fibonacci Numbers to Print? "))

for i in range(print_time):
    a = b
    b = fib
    fib = a+b
    print(fib, end = ',')
