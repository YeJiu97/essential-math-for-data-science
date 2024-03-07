from sympy import *
from sympy.plotting import plot3d

# 向SymPy声明变量x和y
x, y = symbols('x y')

# 现在使用Python语法声明函数
f = x ** 2 + y ** 2

# 计算 x 和 y 的偏导数
dfx = diff(f, x)
dfy = diff(f, y)

# 打印结果
print(dfx)
print(dfy)

# 绘制函数
plot3d(f)