#50 random integers each between 3 and 6
from random import randint


for i in range(50):
    a = randint(3,6)
    print(a,end= " ")
