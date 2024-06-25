# 计算给定直线和数据的平方和
import pandas as pd

# 读取数据
points = list(pd.read_csv('https://bit.ly/3goOAnt', delimiter = ',').itertuples())  # list()将迭代器转换为列表

# 长度
n = len(points)

# 使用封闭方程直接计算m和b
m = (n * sum(p.x * p.y for p in points) - sum(p.x for p in points) *
     sum(p.y for p in points)) / (n * sum(p.x ** 2 for p in points) -
                                  sum(p.x for p in points) ** 2)

b = (sum(p.y for p in points) - m * sum(p.x for p in points)) / n


# 封闭方程不能够很好的拓展到更大的数据集，因为它需要计算所有的点的和
# 对于多维的数据集，我们可以使用梯度下降法，不使用封闭方程，因为存在着多个变量

print(m, b)