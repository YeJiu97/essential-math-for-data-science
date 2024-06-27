from sympy import symbols, Function, Sum, log, exp, diff, lambdify
import pandas as pd

# Load the data
points = list(pd.read_csv("https://tinyurl.com/y2cocoo7").itertuples())

# Define the symbols for coefficients, index, and total number of points
b1, b0, i, n = symbols('b1 b0 i n')

# Define symbols for functions representing x and y values
x, y = symbols('x y', cls=Function)

# Define the joint likelihood function using symbolic computation
joint_likelihood = Sum(
    log(
        (1.0 / (1.0 + exp(-(b0 + b1 * x(i))))) ** y(i) *
        (1.0 - (1.0 / (1.0 + exp(-(b0 + b1 * x(i)))))) ** (1 - y(i))
    ), (i, 0, n)
)

# Compute the partial derivative with respect to b1
d_b1 = diff(joint_likelihood, b1) \
    .subs(n, len(points) - 1) \
    .doit() \
    .replace(x, lambda i: points[i].x) \
    .replace(y, lambda i: points[i].y)

# Compute the partial derivative with respect to b0
d_b0 = diff(joint_likelihood, b0) \
    .subs(n, len(points) - 1) \
    .doit() \
    .replace(x, lambda i: points[i].x) \
    .replace(y, lambda i: points[i].y)

# Convert symbolic expressions to numerical functions for faster computation
d_b1 = lambdify([b1, b0], d_b1)
d_b0 = lambdify([b1, b0], d_b0)

# Initialize coefficients
b1 = 0.01
b0 = 0.01
learning_rate = 0.01

# Perform Gradient Descent
for j in range(10_000):
    b1 += d_b1(b1, b0) * learning_rate
    b0 += d_b0(b1, b0) * learning_rate

# Output the results
print(b1, b0)
# Expected output: 0.6926693075370812, -3.175751550409821
