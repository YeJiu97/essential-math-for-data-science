# 通过逼近来计算斜率

def derivative(f, x, step_size):
    m = (f(x + step_size) - f(x)) / step_size   # (y_2 - y_1) / (x_2 - x_1
    return m

def my_function(x):
    return x ** 2

slope_at_2 = derivative(my_function, 2, 0.000000001)
print(slope_at_2)