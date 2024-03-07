# 实现导数求导
from sympy import *
from sympy.plotting import plot3d

# 函数
x, y = symbols('x y')
f = 2 * x ** 3 + 3 * y ** 3

# 求导
df_x = diff(f, x)
df_y = diff(f, y)

# 打印结果
print(df_x)
print(df_y)

# 绘制函数
plot3d(f)