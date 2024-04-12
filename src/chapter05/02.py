# 计算每个点的残差
import pandas as pd

# 读取数据
points = pd.read_csv('https://bit.ly/3goOAnt', delimiter=',').itertuples

# 查看一下points
print(points)

# 根据给定的直线执行测试
m = 1.9393
b = 4.7333

# 计算每个点的残差
for p in points():
    y_actual = p.y
    y_predict = m * p.x + b
    residuals = y_actual - y_predict
    print(f'x={p.x}, y={p.y}, y_predict={y_predict}, residual={residuals}')