# 残差是直线和点之间的数值差
# 最小化残差的平方和，即最小化误差的平方和
# 误差的平方和是残差的平方和的平均值

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 读取数据
points = pd.read_csv('https://bit.ly/3goOAnt', delimiter = ',').itertuples() # iterrows()方法返回一个迭代器，可以用来遍历数据框的行

# 根据给定的直线执行测试
m = 1.93
b = 4.73

# 计算残差
for p in points:
    y_actual = p.y
    y_predict = m*p.x + b
    residual = y_actual - y_predict
    print(f'Actual: {y_actual}, Predicted: {y_predict}, Residual: {residual}')


# 将平方可视化
residuals = [p.y - m*p.x - b for p in points]
plt.plot(residuals)

# 计算误差的平方和
squared_error = np.sum([r**2 for r in residuals])
print(f'误差的平方和: {squared_error}')

plt.show()