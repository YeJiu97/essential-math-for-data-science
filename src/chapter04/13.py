from sympy import *

A = Matrix([
    [4, 2, 4],
    [5, 3, 7],
    [9, 3, 6]
])

B = Matrix([44, 56, 72])

X = A.inv() * B

print(X)
