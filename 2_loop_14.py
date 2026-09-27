#print Diamond
n = int(input("Enter wants number: "))

for i in range(1,2*n):
    spaces = abs(n-i)
    stars = (2*n-1) - 2 * spaces
    print(" "* spaces + "*" *stars)

