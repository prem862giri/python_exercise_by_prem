#print Diamond
a = "*"
for i in range(4):
    print(" "* (3-i) + a *(2*i+1))
for i in range(2,-1,-1):
    print(" "*(3-i)+ a *(2*i+1))