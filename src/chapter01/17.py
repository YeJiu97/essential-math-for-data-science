def derivative(f, x, h=1e-6):
    """
    计算函数在给定点的导数
    :param f: 函数
    :param x: 给定点
    :param h: 微小变化量，默认为 1e-6
    :return: 导数的近似值
    """
    # 使用中心差分法计算导数
    df = (f(x + h) - f(x - h)) / (2 * h)
    return df

# 定义一个函数
def f(x):
    return x ** 2

# 计算 f(x) = x^2 在 x=2 处的导数
x = 2
df = derivative(f, x)
print("f'(2) =", df)
