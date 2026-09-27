#Create A

a = "*"

for i in range(3):
    print(" "*(6-i) + a + " "*(2*i-1)*(i>0) +a *(i>0))

print(" "*3+a*7)
for i in range(3):
    outer_space = 2-i
    inner_space = 7+(2*i)
    print(" "*outer_space+a+" "*inner_space+a)