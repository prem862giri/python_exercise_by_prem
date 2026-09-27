#Print a box using loop

a = "*"
b = " "
for i in range(1):
    print(f"{a*20}")
    for j in range(2):
        print(a,b*16,a)
    print(f"{a*20}")