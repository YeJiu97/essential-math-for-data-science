from sympy import *

x, i, n = symbols('x i n')
f = x ** 2 + 1
lower, upper = 0, 1

n_rectangles = 1000  # 小矩形的数量
delta_x = (upper - lower) / n_rectangles

# 创建包含表达式的列表
expressions = [delta_x * f.subs(x, lower + i * delta_x) for i in range(1, n_rectangles + 1)]

# 对表达式列表求和
area = sum(expressions).doit()

print(area)