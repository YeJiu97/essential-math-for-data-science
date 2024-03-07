from sympy import *

# x 和步长s
x, s = symbols("x s")

# 申明函数
f = x ** 2

# 间隔为s的两点之间的斜率
# 代入上升运行公式
slope_f = (f.subs(x, x + s) - f) / ((x + s) - x)
print(slope_f)

# 将2代入x
slop_2 = slope_f.subs(x, 2)
print(slop_2)

# 计算 x = 2 处的斜率
# 将步长 _s_ 无线趋近于0
result = limit(slop_2, s, 0)

print(result)  # 4