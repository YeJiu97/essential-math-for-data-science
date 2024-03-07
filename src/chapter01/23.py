from sympy import symbols, Function, diff

# 定义符号变量
x, y = symbols('x y')

# 定义 y 关于 x 的函数 y(x)
y_func = Function('y')(x)

# 定义 z 关于 y 的函数 z(y)
z_func = Function('z')(y_func)

# 使用链式法则对 z 关于 x 求导
dz_dx_chain_rule = diff(z_func.subs(y_func, y_func), x).subs(diff(y_func, x), y_func.diff(x))

# 使用非链式法则对 z 关于 x 求导
dz_dx_non_chain_rule = diff(z_func.subs(y_func, y_func), x)

# 输出结果
print("使用链式法则求导得到的结果：", dz_dx_chain_rule)
print("使用非链式法则求导得到的结果：", dz_dx_non_chain_rule)