#Ask user for their name and how many times to print.
name = input("Enter your Name: ")
print_time = int(input("How many times to print your name? "))

for i in range(print_time):
    print(name)