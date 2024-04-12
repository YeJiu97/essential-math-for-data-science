# 使用逆矩阵和转置矩阵来拟合线性方程
import numpy as np
import pandas as pd
from numpy.linalg import inv

# 读取数据
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=',')

# 提取输入变量
X = df.values[:, :-1].flatten()

# 添加占位符1列，以便计算截距
X_1 = np.array([np.ones(len(X)), X]).T

# 提取输入列
Y = df.values[:, -1]

# 计算斜率与截距系数
b = inv(X_1.transpose() @ X_1) @ (X_1.transpose() @ Y)  # @ is the matrix multiplication operator

print(f'相关系数: {b[1]}')
print(f'截距: {b[0]}')