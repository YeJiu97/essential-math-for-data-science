# 使用scikit-learn来执行线性回归
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 读取数据
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=',')

# 提取输入变量
X = df.values[:, :-1]

# 提取输出列
Y = df.values[:, -1]

# 将这些数据拟合为线性回归模型
fit = LinearRegression().fit(X, Y)

# 相关系数
m = fit.coef_.flatten()
b = fit.intercept_.flatten()
print(f'相关系数: {m}')
print(f'截距: {b}')

# 绘制数据和拟合线
plt.scatter(X, Y, color='blue')
plt.plot(X, fit.predict(X), color='red')
plt.show()
