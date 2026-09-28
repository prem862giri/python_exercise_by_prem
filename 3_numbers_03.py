#generate random number between 1 and 10, print your name that many times
from random import randint

n = randint(1,10)
print(n)

for i in range(n):
    print(f"Your name: {i+1}")