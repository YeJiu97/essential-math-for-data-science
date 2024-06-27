import math

def predict_probability(x, b0, b1):
    p = 1.0 / (1.0 + math.exp(-b0 - b1 * x))

# 假设b0 = -2.823，b1 = 0.62，进行可视化
from sympy import *

b0, b1, x = symbols('b0 b1 x')

p = 1.0 / (1.0 + exp(-b0 - b1 * x))

p = p.subs(b0, -2.823)
p = p.subs(b1, 0.62)

print(p)

plot(p)