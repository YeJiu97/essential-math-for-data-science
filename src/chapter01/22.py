# 链式法则
from sympy import *

x = symbols('x')

z = (x ** 2 + 1) ** 3 - 1

dz_dx = diff(z, x)

print(dz_dx)

print("=================================================")
print("=================================================")
print("=================================================")

x = symbols('x')
y = symbols('y')  # 声明符号 y
z = y ** 3 - 2

# 计算 z 关于 y 的导数
dz_dy = diff(z, y)

# 将 y 表达为 x 的函数
y_expr = x ** 2 + 1

# 计算 y 对 x 的导数
dy_dx = diff(y_expr, x)

# 使用链式法则计算 z 对 x 的导数
dz_dx = dz_dy * dy_dx

print(dz_dx)
