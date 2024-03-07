from sympy import Symbol, diff

# 定义符号变量
x = Symbol('x')

# 定义函数
f = x**2

# 计算函数的导数
f_prime = diff(f, x)

print("f'(x) =", f_prime)