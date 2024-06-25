# 基于SymPy的线性回归梯度下降
from sympy import *

m, b, i, n = symbols('m b i n')
x, y = symbols('x y', cls = Function)

# Define the equation
sum_of_squares = Sum((m * x(i) + b - y(i))**2, (i, 0, n))

# Partial derivative with respect to m
D_m = diff(sum_of_squares, m)

# Partial derivative with respect to b
D_b = diff(sum_of_squares, b)

# print
print(D_m)
print(D_b)