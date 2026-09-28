#random x between 1 and 50, y between 2 and 5, computes x**y
from random import randint

x = randint(1,50)
print(x)

y = randint(2,5)
print(y)

print(f"The power y {y} of x {x} is {x**y}")