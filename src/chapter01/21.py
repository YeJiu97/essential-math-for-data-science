from sympy import *

x, s = symbols('x s')
f = x**2
slope_f = (f.subs(x, x+s) - f) / ((x + s) -x)

result = limit(slope_f, s, 0)

print(result)