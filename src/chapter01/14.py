from sympy import *

# 向sympy声明x是一个符号
x = symbols('x')

# 现在使用Python语法来定义一个函数
f = x ** 2

# 计算函数的导数
dx_f = diff(f)
print(dx_f)
print(dx_f)