# 使用scikit-learn来执行线性回归

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 读取数据
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter = ',')

# 提取输入变量
X = df.values[:, :-1]  # 除最后一列之外的所有列

# 提取输出变量
y = df.values[:, -1]  # 最后一列，代码解释，冒号 : 表示选择所有行

# 创建线性回归对象
fit = LinearRegression().fit(X, y)  # 训练模型

# 输出模型参数
m = fit.coef_.flatten()  # 斜率
b = fit.intercept_.flatten()  # 截距

# 输出模型参数
print('斜率:', m)
print('截距:', b)

# 绘制数据
plt.scatter(X, y, color = 'blue', label = 'Data')
plt.plot(X, m*X + b, color = 'red', label = 'Regression Line')
plt.show()