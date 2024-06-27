import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import pandas as pd

# 加载数据
df = pd.read_csv("https://bit.ly/33ebs2R", delimiter = ',')

# 仅使用第一个特征和输出变量
X = df.iloc[:, 0].values.reshape(-1, 1)  # 重塑数据格式适应模型要求
Y = df.iloc[:, -1].values

# 创建并拟合逻辑斯蒂回归模型
model = LogisticRegression(penalty=None)
model.fit(X, Y)

# 生成预测概率的数据点
X_test = np.linspace(X.min(), X.max(), 300).reshape(-1, 1)  # 生成足够密集的点以绘制平滑曲线
probabilities = model.predict_proba(X_test)[:, 1]  # 提取类别1的预测概率

# 绘制预测概率曲线
plt.plot(X_test, probabilities, label='Predicted Probability')
plt.scatter(X, Y, color='red', label='Data Points')  # 原始数据点
plt.xlabel('Feature 1')
plt.ylabel('Probability')
plt.title('Logistic Regression Probability Curve')
plt.legend()
plt.show()
