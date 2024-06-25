# 回归
# 回归是指对连续型的数据进行预测，比如房价、销售额等。回归问题的目标是找到输入变量和输出变量之间的关系，以便预测新的输出变量值。
# 线性回归
# 线性回归是一种最简单的回归方法，它假设输入变量和输出变量之间的关系是线性的，即y = wx + b。

# 线性回归的一个可视化的例子
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 3 * X + 4 + np.random.randn(100, 1)

# 可视化数据
plt.scatter(X, y)
plt.xlabel('X')
plt.ylabel('y')
plt.show()

# 使用线性回归模型拟合数据
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X, y)

# 可视化拟合结果
plt.scatter(X, y)
plt.plot(X, lin_reg.predict(X), color='r')
plt.xlabel('X')
plt.ylabel('y')
plt.show()