# 使用逆矩阵和转置矩阵来拟合线性回归

import numpy as np
import pandas as pd
from numpy.linalg import inv

# 导入数据点
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter = ',')

# 提取输入变量（所有行，除最后一列外的所有列）
X = df.values[:, :-1].flatten()

# 添加占位符1到输入变量中，用来产生截距
# 因为我们要拟合的方程是y = mx + b，而不是y = mx
X_1 = np.vstack([X, np.ones(len(X))]).T

# 提取输出列
Y = df.values[:, -1]

# 计算斜率和截距系数
b = inv(X_1.T.dot(X_1)).dot(X_1.T).dot(Y)
print(b)

y_predict = X_1.dot(b)