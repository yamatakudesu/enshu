a11 = 1.0
a12 = 3.0
a21 = 2.0
a22 = 2.0
b1 = 1.0
b2 = 0.0

x1 = (a22*b1-a12*b2) / (a11*a22-a12*a21)
x2 = (-a21*b1+a11*b2) / (a11*a22-a12*a21)

print(x1, x2)
