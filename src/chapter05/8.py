# QR 分解来执行线性回归
import numpy as np
import pandas as pd
from numpy.linalg import qr, inv

# 导入数据点
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter = ',')

# 提取输入变量（所有行，除最后一列外的所有列）
X = df.values[:, :-1].flatten()

# 添加占位符1到输入变量中，用来产生截距
X_1 = np.vstack([X, np.ones(len(X))]).T

# 提取输出列
Y = df.values[:, -1]

# 计算QR分解
Q, R = qr(X_1)
b = inv(R).dot(Q.T).dot(Y)

print(b)