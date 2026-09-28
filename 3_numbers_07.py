#enter an angle between -180 degree to 180 degree
#with modulo operator, convert it into 0 degree to 360 degree

from math import degrees

user_entered = int(input("Enter a degrees between -180 to 180: "))

converted_degree = user_entered % 360

print(f"{user_entered} degree is also called {converted_degree} degree")