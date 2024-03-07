from sympy import *

# 想sympy声明x
x = symbols('x')

# 现在使用Python语法声明函数
f = x ** 2 + 1

# 计算函数关于x的积分
area = integrate(f, (x, 0, 1))

# 打印结果
print(area)