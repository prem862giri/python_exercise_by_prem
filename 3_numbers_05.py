#generate 50 random number first number between 1 and 2, second between 1 and 3
#third between 1 and 4 and so on.

from random import randint

for i in range(50):
    a = randint(1,i+1)
    print(a)