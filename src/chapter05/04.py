# 使用封闭式方程
import pandas as pd

# 读取数据
points = list(pd.read_csv('https://bit.ly/3goOAnt', delimiter=',').itertuples())

n = len(points)

# 计算m
m = (n * sum([p.x * p.y for p in points]) - sum([p.x for p in points]) * sum([p.y for p in points])) / \
    (n * sum([p.x ** 2 for p in points]) - sum([p.x for p in points]) ** 2)

# 计算b
b = (sum([p.y for p in points]) - m * sum([p.x for p in points])) / n

print(f'相关系数: {m}')
print(f'截距: {b}')

# 使用第三方库进行验证
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([p.x for p in points]).reshape(-1, 1)
Y = np.array([p.y for p in points])

fit = LinearRegression().fit(X, Y)

print(f'相关系数: {fit.coef_.flatten()}')
print(f'截距: {fit.intercept_.flatten()}')