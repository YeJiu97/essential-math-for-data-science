import pandas as pd
from sympy import *

# Import points from CSV
points = list(pd.read_csv("https://bit.ly/2KF29Bd").itertuples())

# Define symbols
m, b, i, n = symbols('m b i n')
x, y = symbols('x y', cls=Function)

# Define sum of squares
sum_of_squares = Sum((m*x(i) + b - y(i)) ** 2, (i, 0, n))

# Calculate derivatives
d_m = diff(sum_of_squares, m) \
    .subs(n, len(points) - 1).doit() \
    .replace(x, lambda i: points[i].x) \
    .replace(y, lambda i: points[i].y)

d_b = diff(sum_of_squares, b) \
    .subs(n, len(points) - 1).doit() \
    .replace(x, lambda i: points[i].x) \
    .replace(y, lambda i: points[i].y)

# Compile using lambdify for faster computation
d_m = lambdify([m, b], d_m)
d_b = lambdify([m, b], d_b)

# Building the model
m = 0.0
b = 0.0

# The learning Rate
L = 0.001

# The number of iterations
iterations = 100_000

# Perform Gradient Descent
for i in range(iterations):
    # Update m and b
    m -= d_m(m, b) * L
    b -= d_b(m, b) * L

print(f"y = {m:.6f}x + {b:.6f}")