#Ask the users for an hour between 1 and 12
#How many hours in future they wants to go
#Print what the hour will be that many hours into the future. 

hour = int(input("Enter hour: "))
hour_ahead = int(input("How many hours ahead? "))

new_hour = (hour + hour_ahead) -12

print(f"New hour: {new_hour} o'clock")