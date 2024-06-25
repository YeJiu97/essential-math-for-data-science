# 计算标准误差
import pandas as pd
from math import sqrt

# 读取数据
points = list(pd.read_csv('https://bit.ly/2KF29Bd', delimiter = ',').itertuples())

# 数量
n = len(points)

# 回归直线
m = 1.939
b = 4.733

# 计算估计值的标准差
S_e = sqrt((sum((p.y - (m*p.x +b))**2 for p in points))/(n-2))

# 打印结果
print(S_e)