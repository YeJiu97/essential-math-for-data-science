# 无穷
from sympy import *

x = symbols('x')
f = 1 / x
result = limit(f, x, oo)

print(result)


# 计算欧拉数
from sympy import *

n = symbols('n') # 创建一个n符号
f = (1 + 1 / n) ** n  # 定义一个函数，这个函数是欧拉数的极限
result = limit(f, n, oo)  # 计算极限

print(result)  # 打印结果
print(result.evalf())  # 打印结果的浮点数形式
